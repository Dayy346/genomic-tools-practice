import vcfpy

def parse_vcf(file_path):
    reader = vcfpy.Reader.from_path(file_path)
    for record in reader:
        print(f"Chromosome: {record.CHROM}, Position: {record.POS}, Ref: {record.REF}, Alt: {record.ALT}")

if __name__ == "__main__":
    parse_vcf("example-4.1.vcf")
