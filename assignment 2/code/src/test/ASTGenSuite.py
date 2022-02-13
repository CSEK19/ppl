import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
   def test_300(self):
       input = '''Class _j{Constructor (_,_4m_q_R6r:_){}Var $o:String ;Val $3O:H=_::$_;}'''
       expect = '''Program([ClassDecl(Id(_j),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(_4m_q_R6r),ClassType(Id(_)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($o),StringType)),AttributeDecl(Static,ConstDecl(Id($3O),ClassType(Id(H)),FieldAccess(Id(_),Id($_))))])])'''
       self.assertTrue(TestAST.test(input,expect,300))


