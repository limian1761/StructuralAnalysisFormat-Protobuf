# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: proto/bsaf.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class ProjectModelGlobalCoordinateSystem(betterproto.Enum):
    X_vertical = 0
    Y_vertical = 1
    Z_vertical = 2
    minus_X_vertical = 3
    minus_Y_vertical = 4
    minus_Z_vertical = 5


class ProjectModelLcsOfCrossSection(betterproto.Enum):
    ZYX = 0
    minusyzx = 1
    minuszminusyx = 2
    yminuszx = 3
    yzminusx = 4
    minuszyminusx = 5
    minusyminuszminusx = 6
    zminusyminusx = 7


class ProjectModelSystemOfUnits(betterproto.Enum):
    metric = 0
    imperial = 1


class ProjectModelNationalCode(betterproto.Enum):
    gb = 0
    ec_standard_en = 1
    ec_onorm_en = 2
    ec_nbn_en = 3
    ec_bs_en = 4
    ec_cys_en = 5
    ec_csn_en = 6
    ec_ds_en = 7
    ec_nen_en = 8
    ec_sfs_en = 9
    ec_nf_en = 10
    ec_din_en = 11
    ec_eloT_en = 12
    ec_is_en = 13
    ec_uni_en = 14
    ec_lu_en = 15
    ec_ms_en = 16
    ec_ns_en = 17
    ec_pn_en = 18
    ec_sr_en = 19
    ec_ss_en_singaporean = 20
    ec_stn_en = 21
    ec_sisT_en = 22
    ec_une_en = 23
    ec_ss_en_swedish = 24
    ibc = 25
    nbr = 26


class ProjectMaterialType(betterproto.Enum):
    concrete = 0
    steel = 1
    timber = 2
    aluminium = 3
    masonry = 4
    other = 5


class ProjectCrossSectionCrossSectionType(betterproto.Enum):
    parametric = 0
    manufactured = 1
    compound = 2
    general = 3


class ProjectCrossSectionShape(betterproto.Enum):
    circle = 0
    rectangle = 1
    double_rectangle = 2
    triple_rectangle = 3
    rectangle_with_plates = 4
    double_rectangle_with_plates = 5
    I_section = 6
    I_section_with_haunch = 7
    I_section_with_haunch_asymmetric = 8
    T_section = 9
    T_section_with_haunch = 10
    C_section = 11
    L_section = 12
    L_section_opposite = 13
    U_section = 14
    oval = 15
    pipe = 16
    polygon = 17
    trapezoid = 18
    X_section = 19
    Z_section = 20
    box = 21
    double_box = 22
    I_rolled = 23
    I_rolled_asymmetric = 24
    tube = 25
    angle = 26
    channel = 27
    T_tee = 28
    Z_zee = 29
    cold_formed_channel = 30
    cold_formed_channeL_with_lips = 31
    cold_formed_zee = 32
    double_I_section = 33
    double_channeL_ftf = 34
    double_channeL_btb = 35
    starred_angle = 36
    double_angle_btb = 37
    double_angle_ftf = 38
    double_angle_btb_ll = 39
    double_angle_ftf_ll = 40
    four_angle_btb = 41
    four_angle_ftf = 42
    four_angle_I = 43
    double_pipe = 44


class ProjectCrossSectionFormCode(betterproto.Enum):
    true = 0
    false = 1


class ProjectMember1DGeometricalShape(betterproto.Enum):
    line = 0
    circular_arc = 1
    parabolic_arc = 2
    bezier = 3
    spline = 4
    polyline = 5


class ProjectMember1DLCS(betterproto.Enum):
    Y_by_vector = 0
    z_by_vector = 1
    Y_by_point = 2
    z_by_point = 3


class ProjectMember1DSystemine(betterproto.Enum):
    centre = 0
    top = 1
    bottom = 2
    left = 3
    right = 4
    top_left = 5
    top_right = 6
    bottom_left = 7
    bottom_right = 8


class ProjectMember1DBehaviourInAnalysis(betterproto.Enum):
    standard = 0
    axial_force_only = 1
    compression_only = 2
    tension_only = 3


class ProjectMemberVarying1DAlignment(betterproto.Enum):
    centre = 0
    top = 1
    bottom = 2
    left = 3
    right = 4
    top_left = 5
    top_right = 6
    bottom_left = 7
    bottom_right = 8


@dataclass
class Project(betterproto.Message):
    project_info: "ProjectProjectInfo" = betterproto.message_field(1)
    mode: "ProjectModel" = betterproto.message_field(2)
    materials: List["ProjectMaterial"] = betterproto.message_field(3)
    cross_sections: List["ProjectCrossSection"] = betterproto.message_field(4)
    nodes: List["ProjectNode"] = betterproto.message_field(5)
    edges: List["ProjectInternalEdge"] = betterproto.message_field(6)
    member_1_ds: List["ProjectMember1D"] = betterproto.message_field(7)
    member_varying_1_d: "ProjectMemberVarying1D" = betterproto.message_field(8)


@dataclass
class ProjectProjectInfo(betterproto.Message):
    name: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)
    projec_t_nr: str = betterproto.string_field(3)
    created: str = betterproto.string_field(4)
    las_t_update: str = betterproto.string_field(5)
    project_type: str = betterproto.string_field(6)
    project_kind: str = betterproto.string_field(7)
    building_type: str = betterproto.string_field(8)
    status: str = betterproto.string_field(9)
    location: str = betterproto.string_field(10)
    id: str = betterproto.string_field(11)


@dataclass
class ProjectModel(betterproto.Message):
    name: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)
    discipline: str = betterproto.string_field(3)
    level_of_detail: str = betterproto.string_field(4)
    status: str = betterproto.string_field(5)
    owner: str = betterproto.string_field(6)
    revision_number: str = betterproto.string_field(7)
    created: str = betterproto.string_field(8)
    last_update: str = betterproto.string_field(9)
    source_type: str = betterproto.string_field(10)
    source_applicatio: str = betterproto.string_field(11)
    saf_version: str = betterproto.string_field(12)
    source_company: str = betterproto.string_field(13)
    global_coordinate_system: "ProjectModelGlobalCoordinateSystem" = (
        betterproto.enum_field(14)
    )
    lcs_of_cross_section: "ProjectModelLcsOfCrossSection" = betterproto.enum_field(15)
    system_of_units: "ProjectModelSystemOfUnits" = betterproto.enum_field(16)
    national_code: "ProjectModelNationalCode" = betterproto.enum_field(17)
    ignored_objects: str = betterproto.string_field(18)
    id: str = betterproto.string_field(19)


@dataclass
class ProjectMaterial(betterproto.Message):
    name: str = betterproto.string_field(1)
    type: "ProjectMaterialType" = betterproto.enum_field(2)
    subtype: str = betterproto.string_field(3)
    quality: str = betterproto.string_field(4)
    unit_mass: float = betterproto.double_field(5)
    e_modulus: float = betterproto.double_field(6)
    g_modulus: float = betterproto.double_field(7)
    poisson_coefficient: float = betterproto.double_field(8)
    thermal_expansion: float = betterproto.double_field(9)
    design_properties: float = betterproto.double_field(10)
    id: str = betterproto.string_field(11)


@dataclass
class ProjectCrossSection(betterproto.Message):
    name: str = betterproto.string_field(1)
    material: str = betterproto.string_field(2)
    cross_section_type: "ProjectCrossSectionCrossSectionType" = betterproto.enum_field(
        3
    )
    shape: "ProjectCrossSectionShape" = betterproto.enum_field(4)
    parameters: str = betterproto.string_field(5)
    profile: str = betterproto.string_field(6)
    form_code: "ProjectCrossSectionFormCode" = betterproto.enum_field(7)
    description_id: str = betterproto.string_field(8)
    a: float = betterproto.double_field(9)
    iy: float = betterproto.double_field(10)
    iz: float = betterproto.double_field(11)
    it: float = betterproto.double_field(12)
    iw: float = betterproto.double_field(13)
    wply: float = betterproto.double_field(14)
    wplz: float = betterproto.double_field(15)
    id: str = betterproto.string_field(16)
    gen_polygon: str = betterproto.string_field(17)


@dataclass
class ProjectNode(betterproto.Message):
    name: str = betterproto.string_field(1)
    coordinate__x: float = betterproto.double_field(2)
    coordinate__y: float = betterproto.double_field(3)
    coordinate__z: float = betterproto.double_field(4)
    id: str = betterproto.string_field(5)


@dataclass
class ProjectInternalEdge(betterproto.Message):
    name: str = betterproto.string_field(1)
    member_2_d: str = betterproto.string_field(2)
    nodes: str = betterproto.string_field(3)
    segments: str = betterproto.string_field(4)
    parent_id: str = betterproto.string_field(5)
    id: str = betterproto.string_field(6)


@dataclass
class ProjectMember1D(betterproto.Message):
    name: str = betterproto.string_field(1)
    type: str = betterproto.string_field(2)
    cross_section: str = betterproto.string_field(3)
    arbitrary_definition: str = betterproto.string_field(4)
    segments: str = betterproto.string_field(5)
    begin_node: str = betterproto.string_field(6)
    end_node: str = betterproto.string_field(7)
    internal_nodes: str = betterproto.string_field(8)
    length: float = betterproto.double_field(9)
    geometrical_shape: "ProjectMember1DGeometricalShape" = betterproto.enum_field(10)
    lcs: "ProjectMember1DLCS" = betterproto.enum_field(101)
    l_c_s_rotation: float = betterproto.double_field(12)
    coordinate__x: float = betterproto.double_field(13)
    coordinate__y: float = betterproto.double_field(14)
    coordinate__z: float = betterproto.double_field(15)
    system_line: "ProjectMember1DSystemine" = betterproto.enum_field(16)
    structural__y_eccentricity_of_beg__node: float = betterproto.double_field(17)
    structural__z_eccentricity_of_beg__node: float = betterproto.double_field(18)
    structural__y_eccentricity_of_end__node: float = betterproto.double_field(19)
    structural__z_eccentricity_of_end__node: float = betterproto.double_field(20)
    analysis__y_eccentricity_of_beg__node: float = betterproto.double_field(21)
    analysis__z_eccentricity_of_beg__node: float = betterproto.double_field(22)
    analysis__y_eccentricity_of_end__node: float = betterproto.double_field(23)
    analysis__z_eccentricity_of_end__node: float = betterproto.double_field(24)
    layer: str = betterproto.string_field(25)
    behaviour_in_analysis: "ProjectMember1DBehaviourInAnalysis" = (
        betterproto.enum_field(26)
    )
    color: str = betterproto.string_field(27)
    parent_id: str = betterproto.string_field(28)
    id: str = betterproto.string_field(29)


@dataclass
class ProjectMemberVarying1D(betterproto.Message):
    name: str = betterproto.string_field(1)
    cross_sections: str = betterproto.string_field(2)
    span: float = betterproto.double_field(3)
    alignment: "ProjectMemberVarying1DAlignment" = betterproto.enum_field(4)
    id: str = betterproto.string_field(5)