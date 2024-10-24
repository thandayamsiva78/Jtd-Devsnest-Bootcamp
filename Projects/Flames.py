# def solve(boys , girls):
#     remove = []
#     unique = []
#     for b in boys:
#         if b in girls:
#             remove.append(b)
#         else:
#             unique.append(b)
#     for g in girls:
#         if g in boys:
#             remove.append(g)
#         else:
#             unique.append(g)
#     # print(remove)
#     # print(unique)
#     return len(unique)
# boy = [x for x in input("Enter Name 1 : ").lower()]
# girl =[x for x in input("Enter Name 2 : ").lower()]

# print(solve(boy,girl))

# def solve2(relation):
#     result_map = {
#         'F':"Friends",
#         'L':"Lovers",
#         'A':"Affectionate",
#         'M':"Marriage",
#         'E':"Enemies",
#         'S':"Siblings" 
#         }
#     number = solve(boy,girl)
#     for _ in range(number):
#         relation =  relation[1:] + relation[0]
#     return result_map[relation[-1]]
# relation = 'FLAMES'
# print(solve2(relation))


