# -*- coding: utf-8 -*-


from typing import Tuple, Union, List


def Clamp(x, minVal, maxVal):
    # type: (float, float, float) -> float
    pass


class Vector3(object):
    x: float
    y: float
    z: float

    def __init__(self, *args):
        # type: (Union[float, Tuple[float, float, float]]) -> None
        pass

    @staticmethod
    def One():
        # type: () -> 'Vector3'
        pass

    @staticmethod
    def Up():
        # type: () -> 'Vector3'
        pass

    @staticmethod
    def Down():
        # type: () -> 'Vector3'
        pass

    @staticmethod
    def Left():
        # type: () -> 'Vector3'
        pass

    @staticmethod
    def Right():
        # type: () -> 'Vector3'
        pass

    @staticmethod
    def Forward():
        # type: () -> 'Vector3'
        pass

    @staticmethod
    def Backward():
        # type: () -> 'Vector3'
        pass

    def Normalized(self):
        # type: () -> 'Vector3'
        pass

    def Length(self):
        # type: () -> float
        pass

    def LengthSquared(self):
        # type: () -> float
        pass

    def ToTuple(self):
        # type: () -> Tuple[float, float, float]
        pass

    def Normalize(self):
        # type: () -> None
        pass

    def Set(self, x=0.0, y=0.0, z=0.0):
        # type: (float, float, float) -> None
        pass

    @staticmethod
    def Dot(a, b):
        # type: ('Vector3', 'Vector3') -> float
        pass

    @staticmethod
    def Cross(a, b):
        # type: ('Vector3', 'Vector3') -> 'Vector3'
        pass

    def __neg__(self):
        # type: () -> 'Vector3'
        pass

    def __pos__(self):
        # type: () -> 'Vector3'
        pass

    def __add__(self, other):
        # type: (Union['Vector3', float]) -> 'Vector3'
        pass

    def __radd__(self, other):
        # type: (Union['Vector3', float]) -> 'Vector3'
        pass

    def __sub__(self, other):
        # type: (Union['Vector3', float]) -> 'Vector3'
        """ Returns the vector difference of self and other """
        pass

    def __rsub__(self, other):
        # type: (Union['Vector3', float]) -> 'Vector3'
        pass

    def __mul__(self, other):
        # type: (Union['Vector3', float]) -> Union['Vector3', float]
        pass

    def __rmul__(self, other):
        # type: (Union['Vector3', float]) -> Union['Vector3', float]
        pass

    def __div__(self, other):
        # type: (float) -> 'Vector3'
        pass

    def __eq__(self, other):
        # type: ('Vector3') -> bool
        pass

    def __ne__(self, other):
        # type: ('Vector3') -> bool
        pass

    def __repr__(self):
        # type: () -> str
        pass

    def __str__(self):
        # type: () -> str
        pass

    def __getitem__(self, i):
        # type: (int) -> float
        pass


class Quaternion(object):
    def __init__(self, *args):
        # type: (Union[float, Tuple[float, float, float, float]]) -> None
        pass

    @staticmethod
    def Euler(roll=0.0, pitch=0.0, yaw=0.0):
        # type: (float, float, float) -> 'Quaternion'
        pass

    @staticmethod
    def AngleAxis(angle=0.0, axis=Vector3.Up()):
        # type: (float, Vector3) -> 'Quaternion'
        pass

    @staticmethod
    def Dot(a, b):
        # type: ('Quaternion', 'Quaternion') -> float
        pass

    @staticmethod
    def Cross(a, b):
        # type: ('Quaternion', 'Quaternion') -> 'Quaternion'
        pass

    @staticmethod
    def Conjugate(q):
        # type: ('Quaternion') -> 'Quaternion'
        pass

    @staticmethod
    def Inverse(q):
        # type: ('Quaternion') -> 'Quaternion'
        pass

    def Length(self):
        # type: () -> float
        pass

    def LengthSquared(self):
        # type: () -> float
        pass

    def ToTuple(self):
        # type: () -> Tuple[float, float, float, float]
        pass

    def Normalized(self):
        # type: () -> 'Quaternion'
        pass

    def Normalize(self):
        # type: () -> None
        pass

    def EulerAngles(self):
        # type: () -> Tuple[float, float, float]
        pass

    def __neg__(self):
        # type: () -> 'Quaternion'
        pass

    def __pos__(self):
        # type: () -> 'Quaternion'
        pass

    def __add__(self, other):
        # type: (Union['Quaternion', float]) -> 'Quaternion'
        pass

    def __radd__(self, other):
        # type: (Union['Quaternion', float]) -> 'Quaternion'
        pass

    def __sub__(self, other):
        # type: (Union['Quaternion', float]) -> 'Quaternion'
        pass

    def __rsub__(self, other):
        # type: (Union['Quaternion', float]) -> 'Quaternion'
        pass

    def __mul__(self, other):
        # type: (Union['Quaternion', float]) -> Union['Quaternion', float]
        pass

    def __rmul__(self, other):
        # type: (Union['Quaternion', float]) -> Union['Quaternion', float]
        pass

    def __div__(self, other):
        # type: (float) -> 'Quaternion'
        pass

    def __eq__(self, other):
        # type: ('Quaternion') -> bool
        pass

    def __ne__(self, other):
        # type: ('Quaternion') -> bool
        pass

    def __repr__(self):
        # type: () -> str
        pass

    def __str__(self):
        # type: () -> str
        pass


class Matrix(object):
    # Creates a matrix of size numRows * numCols initialized to 0
    def __init__(self, rowNum, colNum):
        # type: (int, int) -> None
        pass

    # Create A Identity Matrix  of rowNum * rowNum
    @staticmethod
    def CreateEye(rowNum):
        # type: (int) -> 'Matrix'
        pass

    @staticmethod
    # Create A Matrix with data ,data should be int or float lists
    def Create(data):
        # type: (List[List[float]]) -> 'Matrix'
        pass

    @staticmethod
    # Create a rotation matrix from euler, according to the sequence xyz sequence
    def FromEulerXYZ(euler):
        # type: (Tuple[float, float, float]) -> 'Matrix'
        pass

    @staticmethod
    # Return back to euler from rotation matrix
    def ToEulerXYZ(mat):
        # type: ('Matrix') -> Tuple[float, float, float]
        pass

    # Set A Zero Matrix to Identity Matrix
    def Eye(self):
        # type: () -> None
        pass

    # Set Matrix Data with int or float lists [[]]
    def SetData(self, data):
        # type: (List[List[float]]) -> None
        pass

    def SetListData(self, data):
        # type: (List[float]) -> None
        pass

    # Create Matix with Quaternion Tuple (x,y,z,w)
    @staticmethod
    def QuaternionToMatrix(wxyz):
        # type: (Tuple[float, float, float, float]) -> 'Matrix'
        pass

    def Copy(self):
        # type: () -> 'Matrix'
        pass

    # Returns the number of rows in the matrix
    @property
    def row(self):
        # type: () -> int
        pass

    # Returns the number of columns in the matrix
    @property
    def col(self):
        # type: () -> int
        pass

    # Returns the value of element (i,j): x[i,j]
    def __getitem__(self, ndxTuple):
        # type: (Tuple[int, int]) -> float
        pass

    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, value):
        # type: (Tuple[int, int], float) -> None
        pass

    def Transpose(self):
        # type: () -> 'Matrix'
        pass

    def Inverse(self):
        # type: () -> 'Matrix'
        pass

    # Decompose (T*R*S)Matrix to translate:(x,y,z) , quaternion:(x,y,z,w) ,scale:(x,y,z)
    # Only When Matrix = T*R*S
    # If Matrix = (T1*R1*S1)(T2*R2*S2) ,use DecomposeByQuaternion instead
    def Decompose(self):
        # type: () -> Tuple[Tuple[float, float, float], Tuple[float, float, float, float], Tuple[float, float, float]]
        pass

    # Decompose (T*R*S)Matrix with its quaternion to translate:(x,y,z)  ,scale:(x,y,z)
    # When Matrix = T*R*S , quaterTuple = R.ToQuaternion().ToTuple()
    # If Matrix = (T1*R1*S1)*(T2*R2*S2)*..., quaterTuple = R1.ToQuaternion()*R2.ToQuaternion()*...
    def DecomposeByQuaternion(self, wxyz):
        # type: (Tuple[float, float, float, float]) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]
        pass

    # return  A Rotation Matrix to Quaternion (x,y,z,w)
    def ToQuaternion(self):
        # type: () -> Tuple[float, float, float, float]
        # https://opensource.apple.com/source/WebCore/WebCore-514/platform/graphics/transforms/TransformationMatrix.cpp
        pass

    @staticmethod
    def matrix4_multiply(lhs, rhs):
        # type: ('Matrix', 'Matrix') -> 'Matrix'
        pass

    # Creates and returns a new matrix that results from matrix addition
    def __add__(self, rhsMatrix):
        # type: ('Matrix') -> 'Matrix'
        pass

    # Creates and returns a new matrix resulting from matrix multiplcation
    def __mul__(self, rhsMatrix):
        # type: ('Matrix') -> 'Matrix'
        pass

    # Creates and returns a new matrix that results from matrix sub
    def __sub__(self, rhsMatrix):
        # type: ('Matrix') -> 'Matrix'
        pass

    def __str__(self):
        # type: () -> str
        pass
