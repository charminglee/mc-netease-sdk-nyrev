# -*- coding: utf-8 -*-
def Clamp(x, minVal, maxVal):
    pass


class Vector3(object):
    def __init__(self, *args):
        pass

    @staticmethod
    def One():
        pass

    @staticmethod
    def Up():
        pass

    @staticmethod
    def Down():
        pass

    @staticmethod
    def Left():
        pass

    @staticmethod
    def Right():
        pass

    @staticmethod
    def Forward():
        pass

    @staticmethod
    def Backward():
        pass

    def Normalized(self):
        pass

    def Length(self):
        pass

    def LengthSquared(self):
        pass

    def ToTuple(self):
        pass

    def Normalize(self):
        pass

    def Set(self, x=0.0, y=0.0, z=0.0):
        pass

    @staticmethod
    def Dot(a, b):
        pass

    @staticmethod
    def Cross(a, b):
        pass

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        pass

    def __rsub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __getitem__(self, i):
        pass

class Quaternion(object):
    def __init__(self, *args):
        pass

    @staticmethod
    def Euler(roll=0.0, pitch=0.0, yaw=0.0):
        pass

    @staticmethod
    def AngleAxis(angle=0.0, axis=Vector3.Up()):
        pass

    @staticmethod
    def Dot(a, b):
        pass

    @staticmethod
    def Cross(a, b):
        pass

    @staticmethod
    def Conjugate(q):
        pass

    @staticmethod
    def Inverse(q):
        pass

    def Length(self):
        pass

    def LengthSquared(self):
        pass

    def ToTuple(self):
        pass

    def Normalized(self):
        pass

    def Normalize(self):
        pass

    def EulerAngles(self):
        pass

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

class Matrix(object):
    # Creates a matrix of size numRows * numCols initialized to 0
    def __init__(self, rowNum, colNum):
        pass

    # Create A Identity Matrix  of rowNum * rowNum
    @staticmethod
    def CreateEye(rowNum):
        pass

    @staticmethod
    # Create A Matrix with data ,data should be int or float lists
    def Create(data):
        pass

    @staticmethod
    # Create a rotation matrix from euler, according to the sequence xyz sequence
    def FromEulerXYZ(euler):
        pass

    @staticmethod
    # Return back to euler from rotation matrix
    def ToEulerXYZ(mat):
        pass

    # Set A Zero Matrix to Identity Matrix
    def Eye(self):
        pass

    # Set Matrix Data with int or float lists [[]]
    def SetData(self, data):
        pass

    def SetListData(self, data):
        pass

    # Create Matix with Quaternion Tuple (x,y,z,w)
    @staticmethod
    def QuaternionToMatrix(wxyz):
        pass

    def Copy(self):
        pass

    # Returns the number of rows in the matrix
    @property
    def row(self):
        pass

    # Returns the number of columns in the matrix
    @property
    def col(self):
        pass

    # Returns the value of element (i,j): x[i,j]
    def __getitem__(self, ndxTuple):
        pass

    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, value):
        pass

    def Transpose(self):
        pass

    def Inverse(self):
        pass

    # Decompose (T*R*S)Matrix to translate:(x,y,z) , quaternion:(x,y,z,w) ,scale:(x,y,z)
    # Only When Matrix = T*R*S
    # If Matrix = (T1*R1*S1)(T2*R2*S2) ,use DecomposeByQuaternion instead
    def Decompose(self):
        pass

    # Decompose (T*R*S)Matrix with its quaternion to translate:(x,y,z)  ,scale:(x,y,z)
    # When Matrix = T*R*S , quaterTuple = R.ToQuaternion().ToTuple()
    # If Matrix = (T1*R1*S1)*(T2*R2*S2)*..., quaterTuple = R1.ToQuaternion()*R2.ToQuaternion()*...
    def DecomposeByQuaternion(self, wxyz):
        pass

    # return  A Rotation Matrix to Quaternion (x,y,z,w)
    def ToQuaternion(self):
        # https://opensource.apple.com/source/WebCore/WebCore-514/platform/graphics/transforms/TransformationMatrix.cpp
        pass

    @staticmethod
    def matrix4_multiply(lhs, rhs):
        pass

    # Creates and returns a new matrix that results from matrix addition
    def __add__(self, rhsMatrix):
        pass

    # Creates and returns a new matrix resulting from matrix multiplcation
    def __mul__(self, rhsMatrix):
        pass

    # Creates and returns a new matrix that results from matrix sub
    def __sub__(self, rhsMatrix):
        pass

    def __str__(self):
        pass
