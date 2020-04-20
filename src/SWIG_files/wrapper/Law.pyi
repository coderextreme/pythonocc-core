from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.Adaptor3d import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColgp import *


class Law_Laws:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class law:
	@overload
	@staticmethod
	def MixBnd(Lin: Law_Linear) -> Law_BSpFunc: ...
	@overload
	@staticmethod
	def MixBnd(Degree: int, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, Lin: Law_Linear) -> TColStd_HArray1OfReal: ...
	@staticmethod
	def MixTgt(Degree: int, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NulOnTheRight: bool, Index: int) -> TColStd_HArray1OfReal: ...
	@staticmethod
	def Reparametrize(Curve: Adaptor3d_Curve, First: float, Last: float, HasDF: bool, HasDL: bool, DFirst: float, DLast: float, Rev: bool, NbPoints: int) -> Law_BSpline: ...
	@staticmethod
	def Scale(First: float, Last: float, HasF: bool, HasL: bool, VFirst: float, VLast: float) -> Law_BSpline: ...
	@staticmethod
	def ScaleCub(First: float, Last: float, HasF: bool, HasL: bool, VFirst: float, VLast: float) -> Law_BSpline: ...

class Law_BSpline(Standard_Transient):
	@overload
	def __init__(self, Poles: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Multiplicities: TColStd_Array1OfInteger, Degree: int, Periodic: Optional[bool] = False) -> None: ...
	@overload
	def __init__(self, Poles: TColStd_Array1OfReal, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Multiplicities: TColStd_Array1OfInteger, Degree: int, Periodic: Optional[bool] = False) -> None: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Copy(self) -> Law_BSpline: ...
	def D0(self, U: float) -> float: ...
	def D1(self, U: float) -> Tuple[float, float]: ...
	def D2(self, U: float) -> Tuple[float, float, float]: ...
	def D3(self, U: float) -> Tuple[float, float, float, float]: ...
	def DN(self, U: float, N: int) -> float: ...
	def Degree(self) -> int: ...
	def EndPoint(self) -> float: ...
	def FirstParameter(self) -> float: ...
	def FirstUKnotIndex(self) -> int: ...
	def IncreaseDegree(self, Degree: int) -> None: ...
	@overload
	def IncreaseMultiplicity(self, Index: int, M: int) -> None: ...
	@overload
	def IncreaseMultiplicity(self, I1: int, I2: int, M: int) -> None: ...
	def IncrementMultiplicity(self, I1: int, I2: int, M: int) -> None: ...
	def InsertKnot(self, U: float, M: Optional[int] = 1, ParametricTolerance: Optional[float] = 0.0, Add: Optional[bool] = True) -> None: ...
	def InsertKnots(self, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, ParametricTolerance: Optional[float] = 0.0, Add: Optional[bool] = False) -> None: ...
	def IsCN(self, N: int) -> bool: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def Knot(self, Index: int) -> float: ...
	def KnotDistribution(self) -> GeomAbs_BSplKnotDistribution: ...
	def KnotSequence(self, K: TColStd_Array1OfReal) -> None: ...
	def Knots(self, K: TColStd_Array1OfReal) -> None: ...
	def LastParameter(self) -> float: ...
	def LastUKnotIndex(self) -> int: ...
	def LocalD0(self, U: float, FromK1: int, ToK2: int) -> float: ...
	def LocalD1(self, U: float, FromK1: int, ToK2: int) -> Tuple[float, float]: ...
	def LocalD2(self, U: float, FromK1: int, ToK2: int) -> Tuple[float, float, float]: ...
	def LocalD3(self, U: float, FromK1: int, ToK2: int) -> Tuple[float, float, float, float]: ...
	def LocalDN(self, U: float, FromK1: int, ToK2: int, N: int) -> float: ...
	def LocalValue(self, U: float, FromK1: int, ToK2: int) -> float: ...
	def LocateU(self, U: float, ParametricTolerance: float, WithKnotRepetition: Optional[bool] = False) -> Tuple[int, int]: ...
	@staticmethod
	def MaxDegree() -> int: ...
	def MovePointAndTangent(self, U: float, NewValue: float, Derivative: float, Tolerance: float, StartingCondition: int, EndingCondition: int) -> int: ...
	def Multiplicities(self, M: TColStd_Array1OfInteger) -> None: ...
	def Multiplicity(self, Index: int) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def PeriodicNormalization(self) -> float: ...
	def Pole(self, Index: int) -> float: ...
	def Poles(self, P: TColStd_Array1OfReal) -> None: ...
	def RemoveKnot(self, Index: int, M: int, Tolerance: float) -> bool: ...
	def Resolution(self, Tolerance3D: float) -> float: ...
	def Reverse(self) -> None: ...
	def ReversedParameter(self, U: float) -> float: ...
	def Segment(self, U1: float, U2: float) -> None: ...
	@overload
	def SetKnot(self, Index: int, K: float) -> None: ...
	@overload
	def SetKnot(self, Index: int, K: float, M: int) -> None: ...
	def SetKnots(self, K: TColStd_Array1OfReal) -> None: ...
	def SetNotPeriodic(self) -> None: ...
	def SetOrigin(self, Index: int) -> None: ...
	def SetPeriodic(self) -> None: ...
	@overload
	def SetPole(self, Index: int, P: float) -> None: ...
	@overload
	def SetPole(self, Index: int, P: float, Weight: float) -> None: ...
	def SetWeight(self, Index: int, Weight: float) -> None: ...
	def StartPoint(self) -> float: ...
	def Value(self, U: float) -> float: ...
	def Weight(self, Index: int) -> float: ...
	def Weights(self, W: TColStd_Array1OfReal) -> None: ...

class Law_BSplineKnotSplitting:
	def __init__(self, BasisLaw: Law_BSpline, ContinuityRange: int) -> None: ...
	def NbSplits(self) -> int: ...
	def SplitValue(self, Index: int) -> int: ...
	def Splitting(self, SplitValues: TColStd_Array1OfInteger) -> None: ...

class Law_Function(Standard_Transient):
	def Bounds(self) -> Tuple[float, float]: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D1(self, X: float) -> Tuple[float, float]: ...
	def D2(self, X: float) -> Tuple[float, float, float]: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def Trim(self, PFirst: float, PLast: float, Tol: float) -> Law_Function: ...
	def Value(self, X: float) -> float: ...

class Law_Interpolate:
	@overload
	def __init__(self, Points: TColStd_HArray1OfReal, PeriodicFlag: bool, Tolerance: float) -> None: ...
	@overload
	def __init__(self, Points: TColStd_HArray1OfReal, Parameters: TColStd_HArray1OfReal, PeriodicFlag: bool, Tolerance: float) -> None: ...
	def Curve(self) -> Law_BSpline: ...
	def IsDone(self) -> bool: ...
	@overload
	def Load(self, InitialTangent: float, FinalTangent: float) -> None: ...
	@overload
	def Load(self, Tangents: TColStd_Array1OfReal, TangentFlags: TColStd_HArray1OfBoolean) -> None: ...
	def Perform(self) -> None: ...

class Law_BSpFunc(Law_Function):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Law_BSpline, First: float, Last: float) -> None: ...
	def Bounds(self) -> Tuple[float, float]: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Curve(self) -> Law_BSpline: ...
	def D1(self, X: float) -> Tuple[float, float]: ...
	def D2(self, X: float) -> Tuple[float, float, float]: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def SetCurve(self, C: Law_BSpline) -> None: ...
	def Trim(self, PFirst: float, PLast: float, Tol: float) -> Law_Function: ...
	def Value(self, X: float) -> float: ...

class Law_Composite(Law_Function):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, First: float, Last: float, Tol: float) -> None: ...
	def Bounds(self) -> Tuple[float, float]: ...
	def ChangeElementaryLaw(self, W: float) -> Law_Function: ...
	def ChangeLaws(self) -> Law_Laws: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D1(self, X: float) -> Tuple[float, float]: ...
	def D2(self, X: float) -> Tuple[float, float, float]: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsPeriodic(self) -> bool: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def SetPeriodic(self) -> None: ...
	def Trim(self, PFirst: float, PLast: float, Tol: float) -> Law_Function: ...
	def Value(self, X: float) -> float: ...

class Law_Constant(Law_Function):
	def __init__(self) -> None: ...
	def Bounds(self) -> Tuple[float, float]: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D1(self, X: float) -> Tuple[float, float]: ...
	def D2(self, X: float) -> Tuple[float, float, float]: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def Set(self, Radius: float, PFirst: float, PLast: float) -> None: ...
	def Trim(self, PFirst: float, PLast: float, Tol: float) -> Law_Function: ...
	def Value(self, X: float) -> float: ...

class Law_Linear(Law_Function):
	def __init__(self) -> None: ...
	def Bounds(self) -> Tuple[float, float]: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D1(self, X: float) -> Tuple[float, float]: ...
	def D2(self, X: float) -> Tuple[float, float, float]: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def Set(self, Pdeb: float, Valdeb: float, Pfin: float, Valfin: float) -> None: ...
	def Trim(self, PFirst: float, PLast: float, Tol: float) -> Law_Function: ...
	def Value(self, X: float) -> float: ...

class Law_Interpol(Law_BSpFunc):
	def __init__(self) -> None: ...
	@overload
	def Set(self, ParAndRad: TColgp_Array1OfPnt2d, Periodic: Optional[bool] = False) -> None: ...
	@overload
	def Set(self, ParAndRad: TColgp_Array1OfPnt2d, Dd: float, Df: float, Periodic: Optional[bool] = False) -> None: ...
	@overload
	def SetInRelative(self, ParAndRad: TColgp_Array1OfPnt2d, Ud: float, Uf: float, Periodic: Optional[bool] = False) -> None: ...
	@overload
	def SetInRelative(self, ParAndRad: TColgp_Array1OfPnt2d, Ud: float, Uf: float, Dd: float, Df: float, Periodic: Optional[bool] = False) -> None: ...

class Law_S(Law_BSpFunc):
	def __init__(self) -> None: ...
	@overload
	def Set(self, Pdeb: float, Valdeb: float, Pfin: float, Valfin: float) -> None: ...
	@overload
	def Set(self, Pdeb: float, Valdeb: float, Ddeb: float, Pfin: float, Valfin: float, Dfin: float) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

law_MixBnd = law.MixBnd
law_MixBnd = law.MixBnd
law_MixTgt = law.MixTgt
law_Reparametrize = law.Reparametrize
law_Scale = law.Scale
law_ScaleCub = law.ScaleCub
Law_BSpline_MaxDegree = Law_BSpline.MaxDegree
