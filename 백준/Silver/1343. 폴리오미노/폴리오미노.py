
st  = input()

st = st.replace('XXXX','AAAA')
st = st.replace('XX','BB')

if 'X' in st:
    print(-1)
else:
    print(st)
