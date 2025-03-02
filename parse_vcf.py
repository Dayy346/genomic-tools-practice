import vcfpy
import csv

def parse_vcf(file_path, output_csv):
    reader = vcfpy.Reader.from_path(file_path)
    with open(output_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Chromosome", "Position", "Reference", "Alternate", "Variant Type"])

        for record in reader:
            for alt in record.ALT:
                writer.writerow([record.CHROM, record.POS, record.REF, alt.value, alt.type_])

if __name__ == "__main__":
    parse_vcf("example-4.1.vcf", "variants.csv")
