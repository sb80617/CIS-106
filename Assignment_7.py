class employee():                  
    def __init__(self, first_name, last_name, salary, bonus = .10 ):
        self.First_name = first_name
        self.Last_name = last_name 
        self.Salary = salary
        self.Bonus = bonus
class manager(employee):
      def __init__(self, first_name, last_name, salary, bonus = .20 ):
           self.First_name = first_name
           self.Last_name = last_name 
           self.Salary = salary
           self.Bonus = bonus
      def long_term(self):
        self.Bonus = .50
jim = manager("jim", "jones", 200000)
print(jim.First_name)
print(jim.Last_name)
print(jim.Salary)
print(jim.Bonus)
jim.long_term()
print(jim.Bonus)