#!/usr/bin/env python
# coding: utf-8

# In[1]:


global facts
global is_changed


# In[2]:


is_changed = True
facts = [["vertebrate","duck"],["flying","duck"],["mammal","cat"]]


# In[3]:


def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True


# In[4]:


while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "mammal":
            assert_fact(["vertebrate",A1[1]])
        if A1[0] == "vertebrate":
            assert_fact(["animal",A1[1]])
        if A1[0] == "vertebrate" and ["flying",A1[1]] in facts:
            assert_fact(["bird",A1[1]])


# In[5]:


print(facts)


# In[ ]:




