import pandas as pd

class Job_Data_Analysis:
    def __init__(self, filename):
        self.df = pd.read_excel(filename)
        print("File loaded successfully!")

    def get_company_locations(self):
        return self.df['company_location'].unique().tolist()

    def get_salary_range_per_emp_type(self, country):
        a = self.df[self.df['company_location'] == country]
        salary = a.groupby('employment_type')['salary_usd'].agg(['min', 'mean', 'max'])
        return salary

    def get_avg_exp_per_level(self, country):
        a = self.df[self.df['company_location'] == country]
        avg = a.groupby('experience_level')['years_experience'].mean().to_dict()
        return avg

    def get_num_industry(self):
        num = self.df.groupby('company_location')['industry'].nunique().to_dict()
        return num

    def get_benefit_score_range(self):
        benefit = self.df.groupby('company_location')['benefits_score'].agg(['min', 'mean', 'max'])
        return benefit

analyzer = Job_Data_Analysis("ai_job_dataset.csv.xlsx")

print("Company Locations:")
print(analyzer.get_company_locations())

print("\nSalary Range in India:")
print(analyzer.get_salary_range_per_emp_type("India"))

print("\nAverage Experience in Germany:")
print(analyzer.get_avg_exp_per_level("Germany"))

print("\nNumber of Industries per Country:")
print(analyzer.get_num_industry())

print("\nBenefit Score Range per Country:")
print(analyzer.get_benefit_score_range())