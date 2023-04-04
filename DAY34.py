#  Day 34 coding Statement : Write a Program to Remove brackets from an algebraic expression

eqn=input("Enter the algebraic equation:")
bracket='(',')'
alg_eqn=""
for i in eqn:
    if i not in bracket:
        alg_eqn=alg_eqn+i
print(alg_eqn)
