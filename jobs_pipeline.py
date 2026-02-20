import pandas as pd
from scraper import check_company_jobs

INPUT_PATH = "data/companies.xlsx"
OUTPUT_PATH = "data/jobs_found.csv"

def main():
    df = pd.read_excel(INPUT_PATH)

    results = []

    for _, row in df.iterrows():
        company = row["Компания"]
        site = row["Сайт"]

        print(f"Checking: {company}")

        matches = check_company_jobs(company, site)

        for match in matches:
            results.append({
                "Компания": company,
                "URL": match
            })

    result_df = pd.DataFrame(results)
    result_df.to_csv(OUTPUT_PATH, index=False)

    print("Done. Results saved to", OUTPUT_PATH)

if __name__ == "__main__":
    main()
