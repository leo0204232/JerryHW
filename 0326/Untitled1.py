
# coding: utf-8

# Q1. Lambda & Map

# In[2]:


a=input('輸入一個數')
num=[int(a)]
list(map(lambda y:y+100,num))


# Q2. 裝飾器(Decorator)

# In[9]:


def document(func):
    def func(a,s):
        m=a*s
        print('multiply:',m)
    return func

@document
def add(a,s):
    return a+s

add(10,2)


# Q3.例外處理

# In[10]:


a=input('請輸入一個整數')
try:
    print(int(a))
except:
    print('出錯,請重新輸入')


# Ｑ4.計算機程式

# In[1]:


from source import calculator

input1=int(input('請輸入第一個數字'))
input2=int(input('請輸入第二個數字'))
f=input('請輸入運算值')

print(calculator.answer(input1,input2,f))

