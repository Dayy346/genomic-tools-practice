import vcf

def parse_vcf(file_path):
    vcf_reader = vcf.Reader(open(file_path, 'r'))
    for record in vcf_reader:
        print(f"Chromosome: {record.CHROM}, Position: {record.POS}, ID: {record.ID}, Ref: {record.REF}, Alt: {record.ALT}")

if __name__ == "__main__":
    parse_vcf("example-4.1.vcf")
