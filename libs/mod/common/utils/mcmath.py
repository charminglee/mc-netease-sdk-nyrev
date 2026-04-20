# -*- coding: utf-8 -*-


from typing import Tuple, List, Any
import math


def Clamp(x, minVal, maxVal):
    # type: (float, float, float) -> float
    pass


class Vector3(object):
    """
    用于表示 3D 向量和点。
    可以使用该结构保存与计算 3D 位置和方向。 此外，它还包含用于执行常见向量操作的函数。
    MC中使用的是右手坐标系，如下图所示。后文中的上下前后左右均是以steve面向z轴正方向得出来的。MC中东西方向为X坐标轴，其中X轴正方向为东，X轴负方向为西；南北方向为Z坐标轴，其中Z轴正方向为南，Z轴负方向为北。即左西右东前南后北。
    """

    def __init__(self, *args):
        # type: (float | Tuple[float, float, float]) -> None
        """
        构造一个向量或者3维点坐标。
        """
        self._x = 0.0 # type: float
        self._y = 0.0 # type: float
        self._z = 0.0 # type: float

    @staticmethod
    def One():
        # type: () -> 'Vector3'
        """
        用于编写 Vector3(1, 1, 1) 的简便方法。
        """
        pass

    @staticmethod
    def Up():
        # type: () -> 'Vector3'
        """
        用于编写 Vector3(0, 1, 0) 的简便方法。
        """
        pass

    @staticmethod
    def Down():
        # type: () -> 'Vector3'
        """
        用于编写 Vector3(0, -1, 0) 的简便方法。
        """
        pass

    @staticmethod
    def Left():
        # type: () -> 'Vector3'
        """
        用于编写 Vector3(-1, 0, 0) 的简便方法，对应MC中的西面。
        """
        pass

    @staticmethod
    def Right():
        # type: () -> 'Vector3'
        """
        用于编写 Vector3(1, 0, 0) 的简便方法，对应MC中的东面。
        """
        pass

    @staticmethod
    def Forward():
        # type: () -> 'Vector3'
        """
        用于编写 Vector3(0, 0, 1) 的简便方法，对应MC中的南面。
        """
        pass

    @staticmethod
    def Backward():
        # type: () -> 'Vector3'
        """
        用于编写 Vector3(0, 0, -1) 的简便方法，对应MC中的北面。
        """
        pass

    @property
    def x(self):
        # type: () -> float
        """
        返回该向量的x坐标值。
        """
        return self._x

    @property
    def y(self):
        # type: () -> float
        """
        返回该向量的y坐标值。
        """
        return self._y

    @property
    def z(self):
        # type: () -> float
        """
        返回该向量的z坐标值。
        """
        return self._z

    def Normalized(self):
        # type: () -> 'Vector3'
        """
        返回长度为 1 时的该向量。
        进行标准化时，向量方向保持不变，但其长度为 1.0。
        请注意，当前向量保持不变，返回一个新的归一化向量。如果 要归一化当前向量，请使用Normalize函数。
        如果向量太小而无法标准化，则返回零向量。
        """
        pass

    def Length(self):
        # type: () -> float
        """
        返回该向量的长度。
        向量长度为 (x*x+y*y+z*z) 的平方根。
        如果只需要比较一些向量的大小， 则可以使用LengthSquared()函数比较它们的平方数（计算平方数更快）。
        """
        pass

    def LengthSquared(self):
        # type: () -> float
        """
        返回该向量的长度的平方。
        """
        pass

    def ToTuple(self):
        # type: () -> Tuple[float, float, float]
        """
        返回该向量的tuple形式(x, y, z)，便于玩家转换后作为其他事件的参数进行传递。
        """
        pass

    def Normalize(self):
        # type: () -> None
        """
        使该向量标准化，向量方向保持不变，但其长度变为 1.0。
        请注意，该函数无返回值，仅改变当前向量，如果要返回当前向量的标准化值且不改变该向量，请使用Normalized函数。
        如果向量太小而无法标准化，则设置为零向量。
        """
        pass

    def Set(self, x=0.0, y=0.0, z=0.0):
        # type: (float, float, float) -> None
        """
        设置该向量的值
        """
        pass

    @staticmethod
    def Dot(a, b):
        # type: ('Vector3', 'Vector3') -> float
        """
        两个向量的点积。
        点积是一个浮点值，它等于 将两个向量的大小相乘，然后乘以向量之间角度的余弦值。
        对于 normalized 向量，如果它们指向完全相同的方向，Dot 返回 1； 如果它们指向完全相反的方向，返回 -1；如果向量彼此垂直，则 Dot 返回 0。
        """
        pass

    @staticmethod
    def Cross(a, b):
        # type: ('Vector3', 'Vector3') -> 'Vector3'
        """
        两个向量的叉积。
        两个向量的叉积生成第三个向量， 该向量垂直于两个输入向量。结果的大小等于： 将两个输入的大小相乘，然后乘以输入之间角度的正弦值。 可以使用“右手定则”确定结果向量的方向。用右手的四指先表示向量a的方向，然后手指朝着手心的方向摆动到向量b的方向，大拇指所指的方向就是向量c的方向。
        """
        pass

    def __neg__(self):
        # type: () -> 'Vector3'
        pass

    def __pos__(self):
        # type: () -> 'Vector3'
        pass

    def __add__(self, other):
        # type: ('Vector3' | float) -> 'Vector3'
        """
        向量加法，两向量相加等于各分量之和。向量与常数相加等于各分量分别加上该常数。
        """
        pass

    def __radd__(self, other):
        # type: ('Vector3' | float) -> 'Vector3'
        """
        向量加法，两向量相加等于各分量之和。向量与常数相加等于各分量分别加上该常数。
        """
        pass

    def __sub__(self, other):
        # type: ('Vector3' | float) -> 'Vector3'
        """
        向量减法，两向量相加等于各分量之差。向量与常数相减等于各分量分别与该常数求差。
        向量求反，返回相反方向的向量
        """
        pass

    def __rsub__(self, other):
        # type: ('Vector3' | float) -> 'Vector3'
        """
        向量减法，两向量相加等于各分量之差。向量与常数相减等于各分量分别与该常数求差。
        向量求反，返回相反方向的向量
        """
        pass

    def __mul__(self, other):
        # type: ('Vector3' | float) -> 'Vector3'
        """
        向量乘法，两向量相乘等于各分量相乘相加，即向量点积，等价于Vector3.Dot(a, b)。向量与常数相乘等于各分量分别乘以该常数。
        """
        pass

    def __rmul__(self, other):
        # type: ('Vector3' | float) -> 'Vector3'
        """
        向量乘法，两向量相乘等于各分量相乘相加，即向量点积，等价于Vector3.Dot(a, b)。向量与常数相乘等于各分量分别乘以该常数。
        """
        pass

    def __div__(self, other):
        # type: (float) -> 'Vector3'
        """
        向量除法，仅支持向量与常数相除，等于各分量分别除以该常数。
        """
        pass

    def __eq__(self, other):
        # type: (Any) -> bool
        """
        判断两个向量是否相等，当各分量均相等时返回True
        """
        pass

    def __ne__(self, other):
        # type: (Any) -> bool
        """
        判断两个向量是否不等，当各分量均相等时返回False
        """
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
    """
    四元数用于表示旋转。
    它们结构紧凑，不受万向锁影响。
    它们基于复数，不容易理解。 您几乎不会有机会访问或修改单个四元数分量（x、y、z、w）
    您可以使用乘法对旋转进行旋转，或对向量进行旋转。
    """

    M_DEGTORAD = math.pi / 180.0
    M_RADTODEG = 1.0 / M_DEGTORAD

    def __init__(self, *args):
        """
        构造一个旋转。
        """
        # type: (float | Tuple[float, float, float, float]) -> None
        self._x = 0.0 # type: float
        self._y = 0.0 # type: float
        self._z = 0.0 # type: float
        self._w = 0.0 # type: float

    @property
    def x(self):
        # type: () -> float
        return self._x

    @property
    def y(self):
        # type: () -> float
        return self._y

    @property
    def z(self):
        # type: () -> float
        return self._z

    @property
    def w(self):
        # type: () -> float
        return self._w

    @staticmethod
    def Euler(x=0.0, y=0.0, z=0.0):
        # type: (float, float, float) -> 'Quaternion'
        """
        创建一个先围绕 Z 轴旋转 z 度、再围绕 X 轴旋转 x 度、最后围绕 Y 轴旋转 y 度的旋转（注意顺序）。注意：如果该欧拉旋转出现万向节锁，会导致四元数返回的EulerAngle异常
        """
        pass

    @staticmethod
    def AngleAxis(angle=0.0, axis=Vector3.Up()):
        # type: (float, Vector3) -> 'Quaternion'
        """
        创建一个围绕 axis 旋转 angle 度的旋转
        """
        pass

    @staticmethod
    def RotationTo(start=Vector3.Up(), end=Vector3.Up()):
        # type: (Vector3, Vector3) -> 'Quaternion'
        pass

    @staticmethod
    def LookDirection(direction=Vector3.Backward(), up=Vector3.Up()):
        # type: (Vector3, Vector3) -> 'Quaternion'
        pass

    @staticmethod
    def Dot(a, b):
        # type: ('Quaternion', 'Quaternion') -> float
        """
        两个旋转的点积。
        点积是一个浮点值，它等于两个旋转对应分量之积求和。
        """
        pass

    @staticmethod
    def Cross(a, b):
        # type: ('Quaternion', 'Quaternion') -> 'Quaternion'
        """
        两个旋转格拉瑟曼积，Cross(a, b)表示旋转a后再旋转p的合成旋转。也可以直接通过a * b得到。
        """
        pass

    @staticmethod
    def Conjugate(q):
        # type: ('Quaternion') -> 'Quaternion'
        """
        返回该旋转的共轭旋转，其w分量不变，其他分量分别取反
        """
        pass

    @staticmethod
    def Inverse(q):
        # type: ('Quaternion') -> 'Quaternion'
        """
        返回该旋转的逆旋转，如果旋转q的模长为1，那么q*q-1将会得到零旋转(0, 0, 0, 1)
        """
        pass

    @property
    def roll(self):
        # type: () -> float
        return 0.0

    @property
    def pitch(self):
        # type: () -> float
        return 0.0

    @property
    def yaw(self):
        # type: () -> float
        return 0.0

    def HasRotation(self):
        # type: () -> bool
        pass

    def Length(self):
        # type: () -> float
        """
        返回该向量的长度。
        向量长度为 (x*x+y*y+z*z) 的平方根。
        如果只需要比较一些向量的大小， 则可以使用LengthSquared()函数比较它们的平方数（计算平方数更快）。
        """
        pass

    def LengthSquared(self):
        # type: () -> float
        """
        返回该向量的长度的平方。
        """
        pass

    def ToTuple(self):
        # type: () -> Tuple[float, float, float, float]
        """
        返回该向量的tuple形式(x, y, z, w)，便于玩家转换后作为其他事件的参数进行传递。
        """
        pass

    def wxyz(self):
        # type: () -> List[float, float, float, float]
        pass

    def Normalized(self):
        # type: () -> 'Quaternion'
        """
        返回该四元数，并且量值为 1。
        进行归一化时，四元数方向保持不变，但其量值为 1.0。
        请注意，当前四元数保持不变，返回一个新的归一化四元数。如果 要归一化原始四元数，请改用Normalize方法。
        如果四元数太小而无法归一化，则会返回(0, 0, 0, 1)，表示零旋转。
        """
        pass

    def Normalize(self):
        # type: () -> None
        """
        使该向量标准化，向量方向保持不变，但其长度变为 1.0。
        请注意，该函数无返回值，仅改变当前向量，如果要返回当前向量的标准化值且不改变该向量，请使用Normalized函数。
        如果向量太小而无法标准化，则设置为零向量。
        """
        pass

    def EulerAngles(self):
        # type: () -> Vector3
        """
        返回围绕 z 轴旋转 euler.z 度、围绕 x 轴旋转 euler.x 度、围绕 y 轴旋转 euler.y 度（按此顺序）的旋转。可以从四元数中读取欧拉角。注意：如果该欧拉旋转出现万向节锁，会导致四元数返回的EulerAngle异常
        """
        pass

    def EulerAnglesZYX(self):
        # type: () -> Vector3
        pass

    def __neg__(self):
        # type: () -> 'Quaternion'
        pass

    def __pos__(self):
        # type: () -> 'Quaternion'
        pass

    def __add__(self, other):
        # type: ('Quaternion' | float) -> 'Quaternion'
        pass

    def __radd__(self, other):
        # type: ('Quaternion' | float) -> 'Quaternion'
        pass

    def __sub__(self, other):
        # type: ('Quaternion' | float) -> 'Quaternion'
        pass

    def __rsub__(self, other):
        # type: ('Quaternion' | float) -> 'Quaternion'
        pass

    def __mul__(self, other):
        # type: ('Quaternion' | Vector3 | float) -> 'Quaternion' | Vector3
        """
        旋转乘法，两个旋转相乘表示先旋转运算符左侧的旋转，再旋转运算符右侧的旋转。等价于Quaternion.Cross(a, b)。不满足乘法交换律，即a*b != b*a
        """
        pass

    def __rmul__(self, other):
        # type: ('Quaternion' | Vector3 | float) -> 'Quaternion' | Vector3
        """
        旋转乘法，两个旋转相乘表示先旋转运算符左侧的旋转，再旋转运算符右侧的旋转。等价于Quaternion.Cross(a, b)。不满足乘法交换律，即a*b != b*a
        """
        pass

    def __div__(self, other):
        # type: (float) -> 'Quaternion'
        pass

    def __eq__(self, other):
        # type: (Any) -> bool
        """
        判断两个旋转是否相等，只有当各分量均相等时返回True
        """
        pass

    def __ne__(self, other):
        # type: (Any) -> bool
        pass

    def __repr__(self):
        # type: () -> str
        pass

    def __str__(self):
        # type: () -> str
        pass


class Matrix(object):
    """
    矩阵（Matrix）是一个按照长方阵列排列的复数或实数集合，在计算机图形学中，常用作物体位置、运动等数学描述
    """

    # Creates a matrix of size numRows * numCols initialized to 0
    def __init__(self, rowNum, colNum):
        # type: (int, int) -> None
        """
        构造一个rowNum行,colNum列的零矩阵。
        """
        self._data = None  # type: List[float] | None
        self._row = rowNum # type: int
        self._col = colNum # type: int

    # Create A Identity Matrix  of rowNum * rowNum
    @staticmethod
    def CreateEye(rowNum):
        # type: (int) -> 'Matrix'
        """
        创建一个单位矩阵
        """
        pass

    @staticmethod
    # Create A Matrix with data ,data should be int or float lists
    def Create(data):
        # type: (List[List[float]]) -> 'Matrix'
        """
        通过数字列表创建一个矩阵
        """
        pass

    @staticmethod
    # Create a rotation matrix from euler, according to the sequence xyz sequence
    def FromEulerXYZ(euler):
        # type: (Tuple[float, float, float]) -> 'Matrix'
        """
        创建欧拉角对应的旋转矩阵，以xyz的旋转顺序应用
        """
        pass

    @staticmethod
    # Return back to euler from rotation matrix
    def ToEulerXYZ(mat):
        # type: ('Matrix') -> Tuple[float, float, float]
        """
        返回矩阵对应的欧拉角
        """
        pass

    # Set A Zero Matrix to Identity Matrix
    def Eye(self):
        # type: () -> None
        """
        把矩阵设置成单位矩阵，要求该矩阵行列数相同，否则报错
        """
        pass

    # Set Matrix Data with int or float lists [[]]
    def SetData(self, data):
        # type: (List[List[float]]) -> None
        """
        根据数据源设置矩阵数据，要求数据源行列大于等于矩阵，否则报错
        """
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
        """
        返回矩阵的拷贝
        """
        pass

    # Returns the number of rows in the matrix
    @property
    def row(self):
        # type: () -> int
        """
        返回矩阵的行数
        """
        return 0

    # Returns the number of columns in the matrix
    @property
    def col(self):
        # type: () -> int
        """
        返回矩阵的列数
        """
        return 0

    # Returns the value of element (i,j): x[i,j]
    def __getitem__(self, ndxTuple):
        # type: (Tuple[int, int]) -> float
        """
        返回矩阵的x行，y列的值,即print mat[x,y]
        """
        pass

    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, value):
        # type: (Tuple[int, int], float) -> None
        """
        设置矩阵x行y列的值，即mat[x,y] = 1
        """
        pass

    def Transpose(self):
        # type: () -> 'Matrix'
        """
        返回转置矩阵
        """
        pass

    def Inverse(self):
        # type: () -> 'Matrix'
        """
        返回逆矩阵，矩阵必须是个方阵，否则函数报错
        """
        pass

    # Decompose (T*R*S)Matrix to translate:(x,y,z) , quaternion:(x,y,z,w) ,scale:(x,y,z)
    # Only When Matrix = T*R*S
    # If Matrix = (T1*R1*S1)(T2*R2*S2) ,use DecomposeByQuaternion instead
    def Decompose(self):
        # type: () -> Tuple[Tuple[float, float, float], Tuple[float, float, float, float], Tuple[float, float, float]]
        """
        对矩阵进行位姿分解，分解成位移向量 * 旋转四元数 * 缩放向量。请注意，并非所有矩阵都可以位姿分解，若矩阵存在非线性变换，强行进行位姿分解会导致信息丢失
        """
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
        """
        返回矩阵的旋转四元数
        """
        pass

    @staticmethod
    def matrix4_multiply(lhs, rhs):
        # type: ('Matrix', 'Matrix') -> 'Matrix'
        """
        返回两个4*4矩阵相乘后结果
        """
        pass

    # Creates and returns a new matrix that results from matrix addition
    def __add__(self, rhsMatrix):
        # type: ('Matrix') -> 'Matrix'
        """
        矩阵加法，两个矩阵相加表示向量的平移、多项式运算等，满足交换律、结合律，且要求两个矩阵行列数量相同
        """
        pass

    # Creates and returns a new matrix resulting from matrix multiplcation
    def __mul__(self, rhsMatrix):
        # type: ('Matrix') -> 'Matrix'
        """
        矩阵乘法，两个矩阵相乘表示线性映射、变换、多项式运算等，不满足交换律，但是满足结合律，且要求两个矩阵行列数量对应
        """
        pass

    # Creates and returns a new matrix that results from matrix sub
    def __sub__(self, rhsMatrix):
        # type: ('Matrix') -> 'Matrix'
        """
        矩阵减法，两个矩阵相加表示向量的平移、多项式运算等，满足交换律、结合律，且要求两个矩阵行列数量相同
        """
        pass

    def __str__(self):
        # type: () -> str
        """
        用于输出矩阵的字符串形式，即print(matrix)
        """
        pass
