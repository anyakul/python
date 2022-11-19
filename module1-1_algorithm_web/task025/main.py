from User import User

natalia = User(identifier=12, first_name="Natalia")
natalia.order = {'apple': 10, 'sandwich': 5, 'coffee': 15}
marina = User(identifier=12, first_name="Marina")
marina.order = {'apple': 10, 'toast': 95, 'coffee': 15}

print(natalia.id)  # 12
print(natalia.name)  # 'Natalia'
print(natalia.total_sum())
print(marina.total_sum())
