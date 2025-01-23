import argparse
from proxy_pe_source_generator import ProxyPESourceGenerator

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Generate source code for a proxy PE file')
    arg_parser.add_argument('-f', '--original-pe-file',
                            required=True,
                            help='Path to the original PE file')
    arg_parser.add_argument('-s', '--pe-file-path-in-source-file',
                            help='Path to the PE file in the source file (default: same as original PE file path)')
    arg_parser.add_argument('-o', '--output-directory',
                            default='.',
                            help='Path to the output source directory (default: current directory)')
    arg_parser.add_argument('-e', '--encoding',
                            default='utf-8',
                            help='Encoding of the output files (default: utf-8)')
    args = arg_parser.parse_args()
    generator = ProxyPESourceGenerator(args.original_pe_file, args.pe_file_path_in_source_file)
    generator.generate_source(args.output_directory, args.encoding)
