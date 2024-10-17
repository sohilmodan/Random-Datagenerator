import random
import pandas as pd

class PersonGenerator:
    def __init__(self, age_groups, probabilities, countries):
        if not abs(sum(probabilities) - 1) < 1e-5:
            raise ValueError("Probabilities must sum to 1.")
        
        self.age_groups = age_groups
        self.probabilities = probabilities
        self.countries = countries
        
        # Define a mapping of age groups to their attribute generation functions
        self.attribute_generators = {
            "0-10": self._generate_child,
            "11-20": self._generate_teen,
            "21-30": self._generate_young_adult,
            "31-40": self._generate_adult,
            "41-50": self._generate_adult,
            "51-60": self._generate_adult,
            "61+": self._generate_senior
        }

    def generate_random_person(self):
        age_group = random.choices(self.age_groups, self.probabilities)[0]
        country = random.choice(self.countries)
        return self.attribute_generators[age_group](country)

    def _generate_child(self, country):
        age = random.randint(0, 10)
        height = random.gauss(115, 15)  # Mean = 115 cm, Std Dev = 15
        weight = random.gauss(25, 10)    # Mean = 25 kg, Std Dev = 10
        income = 0
        return self._create_person_dict(age, height, weight, income, country)

    def _generate_teen(self, country):
        age = random.randint(11, 17)
        height = random.gauss(165, 10)  # Mean = 165 cm, Std Dev = 10
        weight = random.gauss(55, 15)    # Mean = 55 kg, Std Dev = 15
        income = random.uniform(0, 5000)
        return self._create_person_dict(age, height, weight, income, country)

    def _generate_young_adult(self, country):
        age = random.randint(18, 30)
        height = random.gauss(175, 7)   # Mean = 175 cm, Std Dev = 7
        weight = random.gauss(70, 10)    # Mean = 70 kg, Std Dev = 10
        income = self._generate_income(country, 35000, 10000)  # Base income for country
        return self._create_person_dict(age, height, weight, income, country)

    def _generate_adult(self, country):
        age = random.randint(31, 50)
        height = random.gauss(175, 7)   # Mean = 175 cm, Std Dev = 7
        weight = random.gauss(80, 15)    # Mean = 80 kg, Std Dev = 15
        income = self._generate_income(country, 50000, 15000)  # Base income for country
        return self._create_person_dict(age, height, weight, income, country)

    def _generate_senior(self, country):
        age = random.randint(51, 100)
        height = random.gauss(170, 7)   # Mean = 170 cm, Std Dev = 7
        weight = random.gauss(70, 10)    # Mean = 70 kg, Std Dev = 10
        income = self._generate_income(country, 30000, 10000)  # Base income for country
        return self._create_person_dict(age, height, weight, income, country)

    def _generate_income(self, country, base_income, std_dev):
        # Adjust income based on country
        country_multiplier = {
            "USA": 1.5,
            "Canada": 1.2,
            "Germany": 1.1,
            "India": 0.9,
            "China": 0.8,
            "Brazil": 0.7
        }
        
        multiplier = country_multiplier.get(country, 1)
        return max(0, random.gauss(base_income * multiplier, std_dev))

    def _create_person_dict(self, age, height, weight, income, country):
        return {
            'age': age,
            'height': round(height, 2),
            'weight': round(weight, 2),
            'income': round(income, 2),
            'country': country
        }

# Example usage
age_groups = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61+"]
probabilities = [0.1, 0.2, 0.2, 0.15, 0.15, 0.1, 0.1]
countries = ["USA", "Canada", "Germany", "India", "China", "Brazil"]

generator = PersonGenerator(age_groups, probabilities, countries)


# Generate random people
random_people = [generator.generate_random_person() for _ in range(2300)]
df=pd.DataFrame(random_people)
df.to_csv('D:\ss\RandomData.csv',index=False)

for person in random_people:
    print(person)
