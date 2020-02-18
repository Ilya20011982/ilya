import pandas as pd

data = pd.read_csv(
    'in.txt',
    sep=';',
    names=['name', 'math', 'physics', 'russian']
)
data['mean'] = data.mean(axis=1)

with open('out.txt', 'w') as f:
    f.write('\n'.join(map(str, data['mean'])) + '\n')
    f.write(' '.join(map(str, data.mean()[:3])))
