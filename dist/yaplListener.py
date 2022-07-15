# Generated from /Users/lpcuellar/Documents/UVG/2022-2/COMPIS/COMPIS-Lab-0/yapl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete listener for a parse tree produced by yaplParser.
class yaplListener(ParseTreeListener):

    # Enter a parse tree produced by yaplParser#program.
    def enterProgram(self, ctx:yaplParser.ProgramContext):
        pass

    # Exit a parse tree produced by yaplParser#program.
    def exitProgram(self, ctx:yaplParser.ProgramContext):
        pass


    # Enter a parse tree produced by yaplParser#classes.
    def enterClasses(self, ctx:yaplParser.ClassesContext):
        pass

    # Exit a parse tree produced by yaplParser#classes.
    def exitClasses(self, ctx:yaplParser.ClassesContext):
        pass


    # Enter a parse tree produced by yaplParser#eof.
    def enterEof(self, ctx:yaplParser.EofContext):
        pass

    # Exit a parse tree produced by yaplParser#eof.
    def exitEof(self, ctx:yaplParser.EofContext):
        pass


    # Enter a parse tree produced by yaplParser#classDefine.
    def enterClassDefine(self, ctx:yaplParser.ClassDefineContext):
        pass

    # Exit a parse tree produced by yaplParser#classDefine.
    def exitClassDefine(self, ctx:yaplParser.ClassDefineContext):
        pass


    # Enter a parse tree produced by yaplParser#method.
    def enterMethod(self, ctx:yaplParser.MethodContext):
        pass

    # Exit a parse tree produced by yaplParser#method.
    def exitMethod(self, ctx:yaplParser.MethodContext):
        pass


    # Enter a parse tree produced by yaplParser#property.
    def enterProperty(self, ctx:yaplParser.PropertyContext):
        pass

    # Exit a parse tree produced by yaplParser#property.
    def exitProperty(self, ctx:yaplParser.PropertyContext):
        pass


    # Enter a parse tree produced by yaplParser#formal.
    def enterFormal(self, ctx:yaplParser.FormalContext):
        pass

    # Exit a parse tree produced by yaplParser#formal.
    def exitFormal(self, ctx:yaplParser.FormalContext):
        pass


    # Enter a parse tree produced by yaplParser#letIn.
    def enterLetIn(self, ctx:yaplParser.LetInContext):
        pass

    # Exit a parse tree produced by yaplParser#letIn.
    def exitLetIn(self, ctx:yaplParser.LetInContext):
        pass


    # Enter a parse tree produced by yaplParser#minus.
    def enterMinus(self, ctx:yaplParser.MinusContext):
        pass

    # Exit a parse tree produced by yaplParser#minus.
    def exitMinus(self, ctx:yaplParser.MinusContext):
        pass


    # Enter a parse tree produced by yaplParser#string.
    def enterString(self, ctx:yaplParser.StringContext):
        pass

    # Exit a parse tree produced by yaplParser#string.
    def exitString(self, ctx:yaplParser.StringContext):
        pass


    # Enter a parse tree produced by yaplParser#isvoid.
    def enterIsvoid(self, ctx:yaplParser.IsvoidContext):
        pass

    # Exit a parse tree produced by yaplParser#isvoid.
    def exitIsvoid(self, ctx:yaplParser.IsvoidContext):
        pass


    # Enter a parse tree produced by yaplParser#while.
    def enterWhile(self, ctx:yaplParser.WhileContext):
        pass

    # Exit a parse tree produced by yaplParser#while.
    def exitWhile(self, ctx:yaplParser.WhileContext):
        pass


    # Enter a parse tree produced by yaplParser#division.
    def enterDivision(self, ctx:yaplParser.DivisionContext):
        pass

    # Exit a parse tree produced by yaplParser#division.
    def exitDivision(self, ctx:yaplParser.DivisionContext):
        pass


    # Enter a parse tree produced by yaplParser#negative.
    def enterNegative(self, ctx:yaplParser.NegativeContext):
        pass

    # Exit a parse tree produced by yaplParser#negative.
    def exitNegative(self, ctx:yaplParser.NegativeContext):
        pass


    # Enter a parse tree produced by yaplParser#boolNot.
    def enterBoolNot(self, ctx:yaplParser.BoolNotContext):
        pass

    # Exit a parse tree produced by yaplParser#boolNot.
    def exitBoolNot(self, ctx:yaplParser.BoolNotContext):
        pass


    # Enter a parse tree produced by yaplParser#lessThan.
    def enterLessThan(self, ctx:yaplParser.LessThanContext):
        pass

    # Exit a parse tree produced by yaplParser#lessThan.
    def exitLessThan(self, ctx:yaplParser.LessThanContext):
        pass


    # Enter a parse tree produced by yaplParser#block.
    def enterBlock(self, ctx:yaplParser.BlockContext):
        pass

    # Exit a parse tree produced by yaplParser#block.
    def exitBlock(self, ctx:yaplParser.BlockContext):
        pass


    # Enter a parse tree produced by yaplParser#id.
    def enterId(self, ctx:yaplParser.IdContext):
        pass

    # Exit a parse tree produced by yaplParser#id.
    def exitId(self, ctx:yaplParser.IdContext):
        pass


    # Enter a parse tree produced by yaplParser#multiply.
    def enterMultiply(self, ctx:yaplParser.MultiplyContext):
        pass

    # Exit a parse tree produced by yaplParser#multiply.
    def exitMultiply(self, ctx:yaplParser.MultiplyContext):
        pass


    # Enter a parse tree produced by yaplParser#if.
    def enterIf(self, ctx:yaplParser.IfContext):
        pass

    # Exit a parse tree produced by yaplParser#if.
    def exitIf(self, ctx:yaplParser.IfContext):
        pass


    # Enter a parse tree produced by yaplParser#case.
    def enterCase(self, ctx:yaplParser.CaseContext):
        pass

    # Exit a parse tree produced by yaplParser#case.
    def exitCase(self, ctx:yaplParser.CaseContext):
        pass


    # Enter a parse tree produced by yaplParser#ownMethodCall.
    def enterOwnMethodCall(self, ctx:yaplParser.OwnMethodCallContext):
        pass

    # Exit a parse tree produced by yaplParser#ownMethodCall.
    def exitOwnMethodCall(self, ctx:yaplParser.OwnMethodCallContext):
        pass


    # Enter a parse tree produced by yaplParser#add.
    def enterAdd(self, ctx:yaplParser.AddContext):
        pass

    # Exit a parse tree produced by yaplParser#add.
    def exitAdd(self, ctx:yaplParser.AddContext):
        pass


    # Enter a parse tree produced by yaplParser#new.
    def enterNew(self, ctx:yaplParser.NewContext):
        pass

    # Exit a parse tree produced by yaplParser#new.
    def exitNew(self, ctx:yaplParser.NewContext):
        pass


    # Enter a parse tree produced by yaplParser#parentheses.
    def enterParentheses(self, ctx:yaplParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by yaplParser#parentheses.
    def exitParentheses(self, ctx:yaplParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by yaplParser#assignment.
    def enterAssignment(self, ctx:yaplParser.AssignmentContext):
        pass

    # Exit a parse tree produced by yaplParser#assignment.
    def exitAssignment(self, ctx:yaplParser.AssignmentContext):
        pass


    # Enter a parse tree produced by yaplParser#false.
    def enterFalse(self, ctx:yaplParser.FalseContext):
        pass

    # Exit a parse tree produced by yaplParser#false.
    def exitFalse(self, ctx:yaplParser.FalseContext):
        pass


    # Enter a parse tree produced by yaplParser#int.
    def enterInt(self, ctx:yaplParser.IntContext):
        pass

    # Exit a parse tree produced by yaplParser#int.
    def exitInt(self, ctx:yaplParser.IntContext):
        pass


    # Enter a parse tree produced by yaplParser#equal.
    def enterEqual(self, ctx:yaplParser.EqualContext):
        pass

    # Exit a parse tree produced by yaplParser#equal.
    def exitEqual(self, ctx:yaplParser.EqualContext):
        pass


    # Enter a parse tree produced by yaplParser#true.
    def enterTrue(self, ctx:yaplParser.TrueContext):
        pass

    # Exit a parse tree produced by yaplParser#true.
    def exitTrue(self, ctx:yaplParser.TrueContext):
        pass


    # Enter a parse tree produced by yaplParser#lessEqual.
    def enterLessEqual(self, ctx:yaplParser.LessEqualContext):
        pass

    # Exit a parse tree produced by yaplParser#lessEqual.
    def exitLessEqual(self, ctx:yaplParser.LessEqualContext):
        pass


    # Enter a parse tree produced by yaplParser#methodCall.
    def enterMethodCall(self, ctx:yaplParser.MethodCallContext):
        pass

    # Exit a parse tree produced by yaplParser#methodCall.
    def exitMethodCall(self, ctx:yaplParser.MethodCallContext):
        pass



del yaplParser