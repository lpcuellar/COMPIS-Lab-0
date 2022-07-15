# Generated from /Users/lpcuellar/Documents/UVG/2022-2/COMPIS/COMPIS-Lab-0/yapl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete generic visitor for a parse tree produced by yaplParser.

class yaplVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by yaplParser#program.
    def visitProgram(self, ctx:yaplParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#classes.
    def visitClasses(self, ctx:yaplParser.ClassesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#eof.
    def visitEof(self, ctx:yaplParser.EofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#classDefine.
    def visitClassDefine(self, ctx:yaplParser.ClassDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#method.
    def visitMethod(self, ctx:yaplParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#property.
    def visitProperty(self, ctx:yaplParser.PropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#formal.
    def visitFormal(self, ctx:yaplParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#letIn.
    def visitLetIn(self, ctx:yaplParser.LetInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#minus.
    def visitMinus(self, ctx:yaplParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#string.
    def visitString(self, ctx:yaplParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#isvoid.
    def visitIsvoid(self, ctx:yaplParser.IsvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#while.
    def visitWhile(self, ctx:yaplParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#division.
    def visitDivision(self, ctx:yaplParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#negative.
    def visitNegative(self, ctx:yaplParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#boolNot.
    def visitBoolNot(self, ctx:yaplParser.BoolNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#lessThan.
    def visitLessThan(self, ctx:yaplParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#block.
    def visitBlock(self, ctx:yaplParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#id.
    def visitId(self, ctx:yaplParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#multiply.
    def visitMultiply(self, ctx:yaplParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#if.
    def visitIf(self, ctx:yaplParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#case.
    def visitCase(self, ctx:yaplParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#ownMethodCall.
    def visitOwnMethodCall(self, ctx:yaplParser.OwnMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#add.
    def visitAdd(self, ctx:yaplParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#new.
    def visitNew(self, ctx:yaplParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#parentheses.
    def visitParentheses(self, ctx:yaplParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#assignment.
    def visitAssignment(self, ctx:yaplParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#false.
    def visitFalse(self, ctx:yaplParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#int.
    def visitInt(self, ctx:yaplParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#equal.
    def visitEqual(self, ctx:yaplParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#true.
    def visitTrue(self, ctx:yaplParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#lessEqual.
    def visitLessEqual(self, ctx:yaplParser.LessEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#methodCall.
    def visitMethodCall(self, ctx:yaplParser.MethodCallContext):
        return self.visitChildren(ctx)



del yaplParser