def aluno_aprovado(freq,acs,prova=0,sub=0,pai=None,extra=0):
    status = {'aprovado':True,'motivo':[]}
    maior_nota = 0
    if freq > 1 or freq  < 0 :
        raise ValueError("tipo errado")
    if min(acs) <0 or max(acs) >10:
        raise ValueError("valor errado")
    if prova < 0 or prova >10:
            raise ValueError("tipo errado")
    if len(acs) == 10:
        pass
    elif(len(acs)>10):
        raise ValueError("numero grande demais") 
    else:
        for c in range(9):
            if acs[c]:
                acs[c] = acs[c]
                print(acs[c])
            else:
                acs[c] = 0
                print(acs[c])
 
    acs=sorted(acs,reverse=True)
   
    maior_nota = acs[:7]
    media = sum(maior_nota)/len(maior_nota)
    status['acs'] = maior_nota
 
    if prova > sub:
        maior_nota_prova = prova
    else:
        maior_nota_prova=sub
    if pai == None:
        nota_final = (media*0.6) + (maior_nota_prova*0.4)+extra
    else:
        nota_final=(media*0.5) + (maior_nota_prova*0.3)+(pai*0.2)+extra
        status['nota']= nota_final
        status
    if(freq<0.75):
        status['aprovado']=False
        status['motivo'].append("faltas")
    if nota_final < 6 :
        status['aprovado']=False
        status['motivo'].append("nota")
    return status


    

    
        
        


import unittest
import hashlib
class TestStringMethods(unittest.TestCase):

     def test_01_reprovado_falta(self):
         resultado = aluno_aprovado(0.6,[8]*10,6,5,None,0)
         self.assertFalse(resultado['aprovado'])
         self.assertTrue('faltas' in resultado['motivo'])
     
     def test_02_aluno_aprovado_soh_acs(self):
         resultado = aluno_aprovado(0.9,[0]*3+[10]*7,0,0,None,0)
         self.assertTrue(resultado['aprovado'])
         resultado = aluno_aprovado(0.8,[10]*7+[0]*3,0,0,None,0)
         self.assertTrue(resultado['aprovado'])
         resultado = aluno_aprovado(0.8,[9]*7+[0]*3,0,0,None,0)
         self.assertFalse(resultado['aprovado'])
         self.assertTrue('nota' in resultado['motivo'])

     def test_03_aluno_aprovado_sem_sub(self):
         resultado = aluno_aprovado(0.9,[8]*10,6,5,None,0)
         self.assertTrue(resultado['aprovado'])
         resultado = aluno_aprovado(0.9,[8]*10,0,0,None,0)
         self.assertFalse(resultado['aprovado'])
         self.assertTrue('nota' in resultado['motivo'])
     

     def test_04_aluno_aprovado_sub(self):
         resultado = aluno_aprovado(0.9,[6]*10,0,6,None,0)
         self.assertTrue(resultado['aprovado'])
         resultado = aluno_aprovado(0.9,[6]*10,0,0,None,0)
         self.assertFalse(resultado['aprovado'])
         self.assertTrue('nota' in resultado['motivo'])
     
     def test_05_aluno_aprovado_pai(self):
         resultado = aluno_aprovado(0.75,[6]*10,6,5,6,0)
         self.assertTrue(resultado['aprovado'])
         resultado = aluno_aprovado(0.75,[6]*10,6,5,0,0)
         self.assertFalse(resultado['aprovado'])
         self.assertTrue('nota' in resultado['motivo'])
     
     def test_06_aluno_aprovado_extra(self):
         resultado = aluno_aprovado(0.75,[6]*10,6,5,5,1)
         self.assertTrue(resultado['aprovado'])
         resultado = aluno_aprovado(0.75,[6]*10,6,5,5,0)
         self.assertFalse(resultado['aprovado'])
         self.assertTrue('nota' in resultado['motivo'])

     def test_06_falta_e_nota(self):
         resultado = aluno_aprovado(0.2,[6]*10,5,5,6,0)
         self.assertFalse(resultado['aprovado'])
         self.assertTrue('nota' in resultado['motivo'])
         self.assertTrue('faltas' in resultado['motivo'])

     def test_07_valores_padrao(self):
         resultado = aluno_aprovado(0.2,[6]*10,5,5,6)
         self.assertFalse(resultado['aprovado'])
         resultado = aluno_aprovado(0.2,[6]*10,5,5)
         self.assertFalse(resultado['aprovado'])
         resultado = aluno_aprovado(0.2,[6]*10,5)
         self.assertFalse(resultado['aprovado'])
         resultado = aluno_aprovado(0.2,[6]*10)
         self.assertFalse(resultado['aprovado'])

     def test_08_erros(self):
         try:
            aluno_aprovado(75,[6]*10,6,5,5,1)
         except Exception:
             pass
         else:
            self.fail('sua função deveria ter dado um erro')

         try:
            aluno_aprovado(0.75,[11]*10,6,5,5,1)
         except Exception:
             pass
         else:
            self.fail('sua função deveria ter dado um erro')

    
         try:
            aluno_aprovado(0.75,[1]*11,6,5,5,1)
         except Exception:
             pass
         else:
            self.fail('sua função deveria ter dado um erro')


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)
runTests()



