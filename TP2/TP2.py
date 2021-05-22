from docplex.mp.model import Model

m = Model(name='unit allocation')

foldyphone = m.continuous_var(name='foldyphone')
tinyphone = m.continuous_var(name='tinyphone')



foldyphonetime = 1.5
tinyphonetime = 2


foldyphoneprod = m.add_constraint(foldyphone >= 500)
tinyphoneprod = m.add_constraint(tinyphone >= 200)
totalprod = m.add_constraint(m.sum([tinyphone*tinyphonetime, foldyphone*foldyphonetime]) <= 2999.5)


m.maximize(foldyphone*900 + tinyphone*1100)



sol = m.solve()

print(sol.display())
#tinyphone.solution_value
#foldyphone.solution_value