#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyopenms import*


# In[2]:


seq=AASequence.fromString("VAKA")


# In[3]:


seq_wz_MonoWeight=seq.getMonoWeight()


# In[4]:


seq_monoweight_2=seq.getMonoWeight(Residue.ResidueType.Full,2)
mz=seq.getMZ(2)


# In[10]:


print(f"The {seq}  With MonoWeight ( Without Water) ==> {seq_wz_MonoWeight}")
print(f"The Peptide With MonoWeight and 2H ==> {seq_monoweight_2} and The MZ ==> {mz}")


# In[12]:


print(f" {seq} Are Consist of :")
resultOfAllMonoWeight=0
for i in seq:
    print(i.getName()+" => "+str(i.getMonoWeight()))
    resultOfAllMonoWeight+=i.getMonoWeight()


# In[13]:


print(f"The Sum of All Amino Acid (VAKA) {resultOfAllMonoWeight}")


# In[8]:


print(f"Is The VAKA == V + A + K + A ? {bool(seq_monoweight_2==resultOfAllMonoWeight)}")


# In[ ]:




