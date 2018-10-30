import sys
import numpy as np
import argparse
from preprocess import *

def get_args():
    parser = argparse.ArgumentParser(description='Generate n-grams and GloVe vectors')
    parser.add_argument('-k', dest='k', type=int, default=6, help='Length of kmer')
    parser.add_argument('-s', dest='s', type=int, default=2, help='Stride of splitting sequences into kmers')
    parser.add_argument('-n', dest='neg_dir', help='Path to the directory of the negative files')
    parser.add_argument('-o', dest='work_dir', help='Directory where output will be stored')
    parser.add_argument('-p', dest='pos_dir', help='Path to the directory of the positive files')
    args = parser.parse_args()
    return args
    
def main():
    args = get_args()
    Pipeline(**args.__dict__).run(input_dir=args.input_dir)

if __name__ == "__main__":
    main()


class Pipeline:
    def __init__(self,
            k,
            s,
            work_dir,
            pos_dir,
            neg_dir,
            **kwargs  # allows some command line arguments to be ignored
    ):
    self.k = k
    self.s = s
    self.work_dir = output_dir
    if not os.path.isdir(self.work_dir):
        os.makedirs(self.work_dir)
    self.pos_dir = pos_dir
    self.neg_dir = neg_dir


    def run(self, input_dir):
        output_dir_list = list()
        output_dir_list.append(self.step_01_gen_kmers())
        output_dir_list.append(self.step_02_qc_reads_with_vsearch(input_dir=output_dir_list[-1]))
                
    
    def initialize_step(self):
        function_name = sys._getframe(1).f_code.co_name
        log = logging.getLogger(name=function_name)
        log.setLevel(logging.WARNING)
        output_dir = create_output_dir(output_dir_name=function_name, parent_dir=self.work_dir, debug=self.debug)
        return log, output_dir

    def complete_step(self, log, output_dir):
        output_dir_list = sorted(os.listdir(output_dir))
        if len(output_dir_list) == 0:
            raise PipelineException('ERROR: no output files in directory "{}"'.format(output_dir))
        return


    def step_01_gen_kmers(self):
        log, output_dir = self.initialize_step()
        if len(os.listdir(output_dir)) > 0:
            log.warning('output directory "%s" is not empty, this step will be skipped', output_dir)
        else:
            pos_files = glob.glob(os.path.join(self.pos_dir, '*'))
            neg_files = glob.glob(os.path.join(self.neg_dir, '*'))
            log.info('Pos files: "%s"' % pos_files)
            log.info('Neg files: "%s"' % neg_files)
            for input_file in pos_files:
                input_name = os.path.splittext(os.path.basename(input_file))[0]
                output_file = os.path.join(output_dir, '%s_%dmer_%dstride' % (input_name, self.k, self.s))
                seq2kmer(input_file, output_file)
                glove_file = '%s_corpus'
                forglove(output_file, glove_file) 
            for input_file in neg_files:
                input_name = os.path.splittext(os.path.basename(input_file))[0]
                output_file = os.path.join(output_dir, '%s_%dmer_%dstride' % (input_name, self.k, self.s))
                seq2kmer(input_file, output_file)
        complete_step(log, output_dir)
        return output_dir

    def step_02_glove(self, input_dir):
        log, output_dir = self.initialize_step()
        if len(os.listdir(output_dir)) > 0:
            log.warning('output directory "%s" is not empty, this step will be skipped', output_dir)
        else:
            
