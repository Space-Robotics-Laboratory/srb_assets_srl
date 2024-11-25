import bpy
import mathutils


# initialize random__normal_ node group
def random__normal__node_group():
    random__normal_ = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="Random (Normal)"
    )

    random__normal_.color_tag = "NONE"
    random__normal_.description = ""
    random__normal_.default_group_node_width = 140

    # random__normal_ interface
    # Socket Value
    value_socket = random__normal_.interface.new_socket(
        name="Value", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    value_socket.default_value = 0.0
    value_socket.min_value = -3.4028234663852886e38
    value_socket.max_value = 3.4028234663852886e38
    value_socket.subtype = "NONE"
    value_socket.attribute_domain = "POINT"

    # Socket Non-Negative
    non_negative_socket = random__normal_.interface.new_socket(
        name="Non-Negative", in_out="INPUT", socket_type="NodeSocketBool"
    )
    non_negative_socket.default_value = True
    non_negative_socket.attribute_domain = "POINT"

    # Socket Mean
    mean_socket = random__normal_.interface.new_socket(
        name="Mean", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    mean_socket.default_value = 0.0
    mean_socket.min_value = -3.4028234663852886e38
    mean_socket.max_value = 3.4028234663852886e38
    mean_socket.subtype = "NONE"
    mean_socket.attribute_domain = "POINT"

    # Socket Std. Dev.
    std__dev__socket = random__normal_.interface.new_socket(
        name="Std. Dev.", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    std__dev__socket.default_value = 1.0
    std__dev__socket.min_value = 0.0
    std__dev__socket.max_value = 3.4028234663852886e38
    std__dev__socket.subtype = "NONE"
    std__dev__socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket = random__normal_.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    seed_socket.default_value = 0
    seed_socket.min_value = 0
    seed_socket.max_value = 2147483647
    seed_socket.subtype = "NONE"
    seed_socket.attribute_domain = "POINT"
    seed_socket.hide_value = True

    # Socket Offset
    offset_socket = random__normal_.interface.new_socket(
        name="Offset", in_out="INPUT", socket_type="NodeSocketInt"
    )
    offset_socket.default_value = 0
    offset_socket.min_value = 0
    offset_socket.max_value = 2147483647
    offset_socket.subtype = "NONE"
    offset_socket.attribute_domain = "POINT"

    # initialize random__normal_ nodes
    # node Frame
    frame = random__normal_.nodes.new("NodeFrame")
    frame.label = "2 * pi * U_2"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # node Frame.003
    frame_003 = random__normal_.nodes.new("NodeFrame")
    frame_003.label = "X_1"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # node Frame.001
    frame_001 = random__normal_.nodes.new("NodeFrame")
    frame_001.label = "sqrt(-2 * ln(U_1))"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # node Math.002
    math_002 = random__normal_.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = "MULTIPLY"
    math_002.use_clamp = False
    # Value_001
    math_002.inputs[1].default_value = 6.2831854820251465

    # node Random Value.001
    random_value_001 = random__normal_.nodes.new("FunctionNodeRandomValue")
    random_value_001.label = "U_2"
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = "FLOAT"
    # Min_001
    random_value_001.inputs[2].default_value = 0.0
    # Max_001
    random_value_001.inputs[3].default_value = 1.0

    # node Math.010
    math_010 = random__normal_.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = "ADD"
    math_010.use_clamp = False
    math_010.inputs[1].hide = True
    math_010.inputs[2].hide = True
    # Value_001
    math_010.inputs[1].default_value = 1.0

    # node Math.005
    math_005 = random__normal_.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = "MULTIPLY"
    math_005.use_clamp = False

    # node Math.004
    math_004 = random__normal_.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = "COSINE"
    math_004.use_clamp = False

    # node Math.008
    math_008 = random__normal_.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = "MULTIPLY"
    math_008.use_clamp = False

    # node Math.007
    math_007 = random__normal_.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = "ADD"
    math_007.use_clamp = False

    # node Math
    math = random__normal_.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = "LOGARITHM"
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 2.7182817459106445

    # node Random Value.002
    random_value_002 = random__normal_.nodes.new("FunctionNodeRandomValue")
    random_value_002.label = "U_1"
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = "FLOAT"
    # Min_001
    random_value_002.inputs[2].default_value = 0.0
    # Max_001
    random_value_002.inputs[3].default_value = 1.0

    # node Math.001
    math_001 = random__normal_.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = "MULTIPLY"
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = -2.0

    # node Math.003
    math_003 = random__normal_.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = "SQRT"
    math_003.use_clamp = False

    # node Group Output
    group_output = random__normal_.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # node Group Input
    group_input = random__normal_.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # node Switch
    switch = random__normal_.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = "FLOAT"

    # node Math.006
    math_006 = random__normal_.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = "MAXIMUM"
    math_006.use_clamp = False
    # Value_001
    math_006.inputs[1].default_value = 0.0

    # Set parents
    math_002.parent = frame
    random_value_001.parent = frame
    math_010.parent = frame
    math_005.parent = frame_003
    math_004.parent = frame_003
    math.parent = frame_001
    random_value_002.parent = frame_001
    math_001.parent = frame_001
    math_003.parent = frame_001

    # Set locations
    frame.location = (-789.8994140625, -466.3039245605469)
    frame_003.location = (-189.27259826660156, -312.6241455078125)
    frame_001.location = (-1020.868408203125, -235.92041015625)
    math_002.location = (138.8717041015625, -30.349945068359375)
    random_value_001.location = (-51.1282958984375, -20.849945068359375)
    math_010.location = (-241.1282958984375, -137.92230224609375)
    math_005.location = (197.912353515625, -20.78594970703125)
    math_004.location = (7.912353515625, -110.67535400390625)
    math_008.location = (210.5360565185547, -105.03559112548828)
    math_007.location = (400.53607177734375, 29.03577995300293)
    math.location = (177.51742553710938, -9.365585327148438)
    random_value_002.location = (-12.482574462890625, 0.1344146728515625)
    math_001.location = (367.5174255371094, -9.365585327148438)
    math_003.location = (557.5174560546875, -20.365585327148438)
    group_output.location = (970.5360717773438, -8.96422004699707)
    group_input.location = (-1399.3758544921875, -91.58724975585938)
    switch.location = (780.5360717773438, 26.53577995300293)
    math_006.location = (590.5360717773438, -88.39610290527344)

    # initialize random__normal_ links
    # random_value_002.Value -> math.Value
    random__normal_.links.new(random_value_002.outputs[1], math.inputs[0])
    # math.Value -> math_001.Value
    random__normal_.links.new(math.outputs[0], math_001.inputs[0])
    # random_value_001.Value -> math_002.Value
    random__normal_.links.new(random_value_001.outputs[1], math_002.inputs[0])
    # math_002.Value -> math_004.Value
    random__normal_.links.new(math_002.outputs[0], math_004.inputs[0])
    # math_003.Value -> math_005.Value
    random__normal_.links.new(math_003.outputs[0], math_005.inputs[0])
    # group_input.Seed -> random_value_002.Seed
    random__normal_.links.new(group_input.outputs[3], random_value_002.inputs[8])
    # group_input.Seed -> math_010.Value
    random__normal_.links.new(group_input.outputs[3], math_010.inputs[0])
    # math_010.Value -> random_value_001.Seed
    random__normal_.links.new(math_010.outputs[0], random_value_001.inputs[8])
    # group_input.Std. Dev. -> math_008.Value
    random__normal_.links.new(group_input.outputs[2], math_008.inputs[0])
    # group_input.Mean -> math_007.Value
    random__normal_.links.new(group_input.outputs[1], math_007.inputs[0])
    # math_008.Value -> math_007.Value
    random__normal_.links.new(math_008.outputs[0], math_007.inputs[1])
    # math_005.Value -> math_008.Value
    random__normal_.links.new(math_005.outputs[0], math_008.inputs[1])
    # math_004.Value -> math_005.Value
    random__normal_.links.new(math_004.outputs[0], math_005.inputs[1])
    # math_001.Value -> math_003.Value
    random__normal_.links.new(math_001.outputs[0], math_003.inputs[0])
    # group_input.Offset -> random_value_001.ID
    random__normal_.links.new(group_input.outputs[4], random_value_001.inputs[7])
    # group_input.Offset -> random_value_002.ID
    random__normal_.links.new(group_input.outputs[4], random_value_002.inputs[7])
    # group_input.Non-Negative -> switch.Switch
    random__normal_.links.new(group_input.outputs[0], switch.inputs[0])
    # math_007.Value -> math_006.Value
    random__normal_.links.new(math_007.outputs[0], math_006.inputs[0])
    # switch.Output -> group_output.Value
    random__normal_.links.new(switch.outputs[0], group_output.inputs[0])
    # math_007.Value -> switch.False
    random__normal_.links.new(math_007.outputs[0], switch.inputs[1])
    # math_006.Value -> switch.True
    random__normal_.links.new(math_006.outputs[0], switch.inputs[2])
    return random__normal_


random__normal_ = random__normal__node_group()


# initialize random__uniform_ node group
def random__uniform__node_group():
    random__uniform_ = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="Random (Uniform)"
    )

    random__uniform_.color_tag = "NONE"
    random__uniform_.description = ""
    random__uniform_.default_group_node_width = 140

    # random__uniform_ interface
    # Socket Value
    value_socket_1 = random__uniform_.interface.new_socket(
        name="Value", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    value_socket_1.default_value = 0.0
    value_socket_1.min_value = -3.4028234663852886e38
    value_socket_1.max_value = 3.4028234663852886e38
    value_socket_1.subtype = "NONE"
    value_socket_1.attribute_domain = "POINT"

    # Socket Min
    min_socket = random__uniform_.interface.new_socket(
        name="Min", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    min_socket.default_value = 0.0
    min_socket.min_value = -3.4028234663852886e38
    min_socket.max_value = 3.4028234663852886e38
    min_socket.subtype = "NONE"
    min_socket.attribute_domain = "POINT"

    # Socket Max
    max_socket = random__uniform_.interface.new_socket(
        name="Max", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    max_socket.default_value = 1.0
    max_socket.min_value = -3.4028234663852886e38
    max_socket.max_value = 3.4028234663852886e38
    max_socket.subtype = "NONE"
    max_socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_1 = random__uniform_.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    seed_socket_1.default_value = 0
    seed_socket_1.min_value = -2147483648
    seed_socket_1.max_value = 2147483647
    seed_socket_1.subtype = "NONE"
    seed_socket_1.attribute_domain = "POINT"
    seed_socket_1.hide_value = True

    # Socket Offset
    offset_socket_1 = random__uniform_.interface.new_socket(
        name="Offset", in_out="INPUT", socket_type="NodeSocketInt"
    )
    offset_socket_1.default_value = 0
    offset_socket_1.min_value = 0
    offset_socket_1.max_value = 2147483647
    offset_socket_1.subtype = "NONE"
    offset_socket_1.attribute_domain = "POINT"

    # initialize random__uniform_ nodes
    # node Group Output
    group_output_1 = random__uniform_.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    # node Group Input
    group_input_1 = random__uniform_.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"

    # node Random Value.011
    random_value_011 = random__uniform_.nodes.new("FunctionNodeRandomValue")
    random_value_011.name = "Random Value.011"
    random_value_011.data_type = "FLOAT"

    # Set locations
    group_output_1.location = (190.0, 0.0)
    group_input_1.location = (-200.0, 0.0)
    random_value_011.location = (0.0, 0.0)

    # initialize random__uniform_ links
    # random_value_011.Value -> group_output_1.Value
    random__uniform_.links.new(random_value_011.outputs[1], group_output_1.inputs[0])
    # group_input_1.Min -> random_value_011.Min
    random__uniform_.links.new(group_input_1.outputs[0], random_value_011.inputs[2])
    # group_input_1.Max -> random_value_011.Max
    random__uniform_.links.new(group_input_1.outputs[1], random_value_011.inputs[3])
    # group_input_1.Offset -> random_value_011.ID
    random__uniform_.links.new(group_input_1.outputs[3], random_value_011.inputs[7])
    # group_input_1.Seed -> random_value_011.Seed
    random__uniform_.links.new(group_input_1.outputs[2], random_value_011.inputs[8])
    return random__uniform_


random__uniform_ = random__uniform__node_group()


# initialize lunarrock node group
def lunarrock_node_group():
    lunarrock = bpy.data.node_groups.new(type="GeometryNodeTree", name="LunarRock")

    lunarrock.color_tag = "GEOMETRY"
    lunarrock.description = ""
    lunarrock.default_group_node_width = 140

    lunarrock.is_modifier = True

    # lunarrock interface
    # Socket Geometry
    geometry_socket = lunarrock.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_2 = lunarrock.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    seed_socket_2.default_value = 0
    seed_socket_2.min_value = 0
    seed_socket_2.max_value = 2147483647
    seed_socket_2.subtype = "NONE"
    seed_socket_2.attribute_domain = "POINT"
    seed_socket_2.force_non_field = True

    # Socket Subdivisions
    subdivisions_socket = lunarrock.interface.new_socket(
        name="Subdivisions", in_out="INPUT", socket_type="NodeSocketInt"
    )
    subdivisions_socket.default_value = 4
    subdivisions_socket.min_value = 0
    subdivisions_socket.max_value = 10
    subdivisions_socket.subtype = "NONE"
    subdivisions_socket.attribute_domain = "POINT"
    subdivisions_socket.force_non_field = True

    # Socket Scale
    scale_socket = lunarrock.interface.new_socket(
        name="Scale", in_out="INPUT", socket_type="NodeSocketVector"
    )
    scale_socket.default_value = (1.0, 1.0, 1.0)
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e38
    scale_socket.subtype = "XYZ"
    scale_socket.attribute_domain = "POINT"
    scale_socket.force_non_field = True

    # Socket Scale STD
    scale_std_socket = lunarrock.interface.new_socket(
        name="Scale STD", in_out="INPUT", socket_type="NodeSocketVector"
    )
    scale_std_socket.default_value = (0.0, 0.0, 0.0)
    scale_std_socket.min_value = 0.0
    scale_std_socket.max_value = 3.4028234663852886e38
    scale_std_socket.subtype = "XYZ"
    scale_std_socket.attribute_domain = "POINT"
    scale_std_socket.force_non_field = True

    # Socket Horizontal Cut
    horizontal_cut_socket = lunarrock.interface.new_socket(
        name="Horizontal Cut", in_out="INPUT", socket_type="NodeSocketBool"
    )
    horizontal_cut_socket.default_value = False
    horizontal_cut_socket.attribute_domain = "POINT"
    horizontal_cut_socket.force_non_field = True

    # Socket Horizontal Cut Offset
    horizontal_cut_offset_socket = lunarrock.interface.new_socket(
        name="Horizontal Cut Offset", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    horizontal_cut_offset_socket.default_value = 0.0
    horizontal_cut_offset_socket.min_value = -3.4028234663852886e38
    horizontal_cut_offset_socket.max_value = 3.4028234663852886e38
    horizontal_cut_offset_socket.subtype = "DISTANCE"
    horizontal_cut_offset_socket.attribute_domain = "POINT"
    horizontal_cut_offset_socket.force_non_field = True

    # initialize lunarrock nodes
    # node Group Input
    group_input_2 = lunarrock.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"

    # node Group Output
    group_output_2 = lunarrock.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True

    # node Set Material
    set_material = lunarrock.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    # Selection
    set_material.inputs[1].default_value = True
    if "LunarRock" in bpy.data.materials:
        set_material.inputs[2].default_value = bpy.data.materials["LunarRock"]

    # node Cube
    cube = lunarrock.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    # Size
    cube.inputs[0].default_value = (1.0, 1.0, 1.0)
    # Vertices X
    cube.inputs[1].default_value = 2
    # Vertices Y
    cube.inputs[2].default_value = 2
    # Vertices Z
    cube.inputs[3].default_value = 2

    # node Subdivision Surface
    subdivision_surface = lunarrock.nodes.new("GeometryNodeSubdivisionSurface")
    subdivision_surface.name = "Subdivision Surface"
    subdivision_surface.boundary_smooth = "ALL"
    subdivision_surface.uv_smooth = "PRESERVE_BOUNDARIES"

    # node Set Position
    set_position = lunarrock.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[1].hide = True
    set_position.inputs[3].hide = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Voronoi Texture
    voronoi_texture = lunarrock.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = "EUCLIDEAN"
    voronoi_texture.feature = "SMOOTH_F1"
    voronoi_texture.normalize = True
    voronoi_texture.voronoi_dimensions = "4D"
    # Vector
    voronoi_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Smoothness
    voronoi_texture.inputs[6].default_value = 0.0
    # Randomness
    voronoi_texture.inputs[8].default_value = 1.0

    # node Vector Math
    vector_math = lunarrock.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = "MULTIPLY"

    # node Position
    position = lunarrock.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    # node Map Range
    map_range = lunarrock.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = False
    map_range.data_type = "FLOAT"
    map_range.interpolation_type = "LINEAR"
    # From Min
    map_range.inputs[1].default_value = 0.0
    # From Max
    map_range.inputs[2].default_value = 1.0
    # To Min
    map_range.inputs[3].default_value = 0.3333333432674408
    # To Max
    map_range.inputs[4].default_value = 1.0

    # node Set Position.001
    set_position_001 = lunarrock.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.inputs[1].hide = True
    set_position_001.inputs[3].hide = True
    # Selection
    set_position_001.inputs[1].default_value = True
    # Offset
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Vector Math.001
    vector_math_001 = lunarrock.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = "MULTIPLY"

    # node Position.001
    position_001 = lunarrock.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    # node Noise Texture
    noise_texture = lunarrock.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = "4D"
    noise_texture.noise_type = "FBM"
    noise_texture.normalize = True
    # Vector
    noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Detail
    noise_texture.inputs[3].default_value = 15.0

    # node Set Shade Smooth
    set_shade_smooth = lunarrock.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = "FACE"
    # Selection
    set_shade_smooth.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth.inputs[2].default_value = True

    # node Frame
    frame_1 = lunarrock.nodes.new("NodeFrame")
    frame_1.name = "Frame"
    frame_1.label_size = 20
    frame_1.shrink = True

    # node Frame.001
    frame_001_1 = lunarrock.nodes.new("NodeFrame")
    frame_001_1.name = "Frame.001"
    frame_001_1.hide = True
    frame_001_1.label_size = 20
    frame_001_1.shrink = True

    # node Frame.002
    frame_002 = lunarrock.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # node Reroute.001
    reroute_001 = lunarrock.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketFloat"
    # node Transform Geometry
    transform_geometry = lunarrock.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = "COMPONENTS"
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[4].hide = True
    # Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Reroute.002
    reroute_002 = lunarrock.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketInt"
    # node Attribute Statistic
    attribute_statistic = lunarrock.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.data_type = "FLOAT_VECTOR"
    attribute_statistic.domain = "POINT"
    attribute_statistic.inputs[1].hide = True
    attribute_statistic.outputs[0].hide = True
    attribute_statistic.outputs[1].hide = True
    attribute_statistic.outputs[2].hide = True
    attribute_statistic.outputs[6].hide = True
    attribute_statistic.outputs[7].hide = True
    # Selection
    attribute_statistic.inputs[1].default_value = True

    # node Position.002
    position_002 = lunarrock.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"

    # node Reroute.003
    reroute_003 = lunarrock.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.socket_idname = "NodeSocketGeometry"
    # node Vector Math.002
    vector_math_002 = lunarrock.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = "DIVIDE"
    # Vector
    vector_math_002.inputs[0].default_value = (1.0, 1.0, 1.0)

    # node Vector Math.003
    vector_math_003 = lunarrock.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = "ADD"

    # node Vector Math.004
    vector_math_004 = lunarrock.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = "SCALE"
    # Scale
    vector_math_004.inputs[3].default_value = -0.5

    # node Group
    group = lunarrock.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = random__normal_
    # Socket_1
    group.inputs[0].default_value = True
    # Socket_2
    group.inputs[1].default_value = 2.25
    # Socket_3
    group.inputs[2].default_value = 0.3333333432674408
    # Socket_5
    group.inputs[4].default_value = 9799

    # node Group.001
    group_001 = lunarrock.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random__uniform_
    # Socket_1
    group_001.inputs[0].default_value = -100000000.0
    # Socket_2
    group_001.inputs[1].default_value = 1000000000.0
    # Socket_4
    group_001.inputs[3].default_value = 10074

    # node Group.002
    group_002 = lunarrock.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = random__normal_
    # Socket_1
    group_002.inputs[0].default_value = True
    # Socket_2
    group_002.inputs[1].default_value = 1.0
    # Socket_3
    group_002.inputs[2].default_value = 0.25
    # Socket_5
    group_002.inputs[4].default_value = 8856

    # node Group.004
    group_004 = lunarrock.nodes.new("GeometryNodeGroup")
    group_004.name = "Group.004"
    group_004.node_tree = random__normal_
    # Socket_1
    group_004.inputs[0].default_value = True
    # Socket_2
    group_004.inputs[1].default_value = 1.25
    # Socket_3
    group_004.inputs[2].default_value = 0.25
    # Socket_5
    group_004.inputs[4].default_value = 2182

    # node Float Curve
    float_curve = lunarrock.nodes.new("ShaderNodeFloatCurve")
    float_curve.name = "Float Curve"
    # mapping settings
    float_curve.mapping.extend = "EXTRAPOLATED"
    float_curve.mapping.tone = "STANDARD"
    float_curve.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve.mapping.clip_min_x = 0.0
    float_curve.mapping.clip_min_y = 0.0
    float_curve.mapping.clip_max_x = 1.0
    float_curve.mapping.clip_max_y = 1.0
    float_curve.mapping.use_clip = True
    # curve 0
    float_curve_curve_0 = float_curve.mapping.curves[0]
    float_curve_curve_0_point_0 = float_curve_curve_0.points[0]
    float_curve_curve_0_point_0.location = (0.0, 0.0)
    float_curve_curve_0_point_0.handle_type = "AUTO"
    float_curve_curve_0_point_1 = float_curve_curve_0.points[1]
    float_curve_curve_0_point_1.location = (0.3333333432674408, 0.10000000149011612)
    float_curve_curve_0_point_1.handle_type = "AUTO_CLAMPED"
    float_curve_curve_0_point_2 = float_curve_curve_0.points.new(1.0, 1.0)
    float_curve_curve_0_point_2.handle_type = "AUTO"
    # update curve after changes
    float_curve.mapping.update()
    # Factor
    float_curve.inputs[0].default_value = 1.0

    # node Group.005
    group_005 = lunarrock.nodes.new("GeometryNodeGroup")
    group_005.name = "Group.005"
    group_005.node_tree = random__normal_
    # Socket_1
    group_005.inputs[0].default_value = True
    # Socket_2
    group_005.inputs[1].default_value = 0.25
    # Socket_3
    group_005.inputs[2].default_value = 0.10000000149011612
    # Socket_5
    group_005.inputs[4].default_value = 2227

    # node Reroute.005
    reroute_005 = lunarrock.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketFloat"
    # node Group.003
    group_003 = lunarrock.nodes.new("GeometryNodeGroup")
    group_003.name = "Group.003"
    group_003.node_tree = random__normal_
    # Socket_1
    group_003.inputs[0].default_value = True
    # Socket_2
    group_003.inputs[1].default_value = 0.15000000596046448
    # Socket_3
    group_003.inputs[2].default_value = 0.02500000037252903
    # Socket_5
    group_003.inputs[4].default_value = 21973

    # node Group.006
    group_006 = lunarrock.nodes.new("GeometryNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = random__normal_
    # Socket_1
    group_006.inputs[0].default_value = True
    # Socket_2
    group_006.inputs[1].default_value = 0.20000000298023224
    # Socket_3
    group_006.inputs[2].default_value = 0.05000000074505806
    # Socket_5
    group_006.inputs[4].default_value = 14855

    # node Reroute.006
    reroute_006 = lunarrock.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.socket_idname = "NodeSocketFloat"
    # node Reroute
    reroute = lunarrock.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketVectorXYZ"
    # node Group.007
    group_007 = lunarrock.nodes.new("GeometryNodeGroup")
    group_007.name = "Group.007"
    group_007.node_tree = random__uniform_
    # Socket_1
    group_007.inputs[0].default_value = -100000000.0
    # Socket_2
    group_007.inputs[1].default_value = 1000000000.0
    # Socket_4
    group_007.inputs[3].default_value = 10781

    # node Group.008
    group_008 = lunarrock.nodes.new("GeometryNodeGroup")
    group_008.name = "Group.008"
    group_008.node_tree = random__normal_
    # Socket_1
    group_008.inputs[0].default_value = True
    # Socket_2
    group_008.inputs[1].default_value = 0.07500000298023224
    # Socket_3
    group_008.inputs[2].default_value = 0.02500000037252903
    # Socket_5
    group_008.inputs[4].default_value = 3267

    # node Group.010
    group_010 = lunarrock.nodes.new("GeometryNodeGroup")
    group_010.name = "Group.010"
    group_010.node_tree = random__normal_
    # Socket_1
    group_010.inputs[0].default_value = True
    # Socket_2
    group_010.inputs[1].default_value = 0.5600000023841858
    # Socket_3
    group_010.inputs[2].default_value = 0.019999999552965164
    # Socket_5
    group_010.inputs[4].default_value = 5038

    # node Group.011
    group_011 = lunarrock.nodes.new("GeometryNodeGroup")
    group_011.name = "Group.011"
    group_011.node_tree = random__normal_
    # Socket_1
    group_011.inputs[0].default_value = True
    # Socket_2
    group_011.inputs[1].default_value = 2.4000000953674316
    # Socket_3
    group_011.inputs[2].default_value = 0.20000000298023224
    # Socket_5
    group_011.inputs[4].default_value = 3147

    # node Group.012
    group_012 = lunarrock.nodes.new("GeometryNodeGroup")
    group_012.name = "Group.012"
    group_012.node_tree = random__normal_
    # Socket_1
    group_012.inputs[0].default_value = True
    # Socket_2
    group_012.inputs[1].default_value = 0.05000000074505806
    # Socket_3
    group_012.inputs[2].default_value = 0.009999999776482582
    # Socket_5
    group_012.inputs[4].default_value = 3622

    # node Frame.003
    frame_003_1 = lunarrock.nodes.new("NodeFrame")
    frame_003_1.name = "Frame.003"
    frame_003_1.label_size = 20
    frame_003_1.shrink = True

    # node Transform Geometry.001
    transform_geometry_001 = lunarrock.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = "COMPONENTS"
    transform_geometry_001.inputs[1].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[4].hide = True
    # Translation
    transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Random Value
    random_value = lunarrock.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = "FLOAT_VECTOR"
    random_value.inputs[0].hide = True
    random_value.inputs[1].hide = True
    random_value.inputs[2].hide = True
    random_value.inputs[3].hide = True
    random_value.inputs[4].hide = True
    random_value.inputs[5].hide = True
    random_value.inputs[6].hide = True
    random_value.outputs[1].hide = True
    random_value.outputs[2].hide = True
    random_value.outputs[3].hide = True
    # Min
    random_value.inputs[0].default_value = (
        -3.1415927410125732,
        -3.1415927410125732,
        -3.1415927410125732,
    )
    # Max
    random_value.inputs[1].default_value = (
        3.1415927410125732,
        3.1415927410125732,
        3.1415927410125732,
    )

    # node Integer
    integer = lunarrock.nodes.new("FunctionNodeInputInt")
    integer.name = "Integer"
    integer.integer = 424242

    # node Delete Geometry
    delete_geometry = lunarrock.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = "FACE"
    delete_geometry.mode = "ALL"

    # node Compare
    compare = lunarrock.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = "FLOAT"
    compare.mode = "ELEMENT"
    compare.operation = "EQUAL"
    # Epsilon
    compare.inputs[12].default_value = 0.0010000000474974513

    # node Position.004
    position_004 = lunarrock.nodes.new("GeometryNodeInputPosition")
    position_004.name = "Position.004"

    # node Separate XYZ.001
    separate_xyz_001 = lunarrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.outputs[0].hide = True
    separate_xyz_001.outputs[1].hide = True

    # node Normal.001
    normal_001 = lunarrock.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"

    # node Boolean Math
    boolean_math = lunarrock.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = "AND"

    # node Separate XYZ.002
    separate_xyz_002 = lunarrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"
    separate_xyz_002.outputs[0].hide = True
    separate_xyz_002.outputs[1].hide = True

    # node Compare.001
    compare_001 = lunarrock.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = "FLOAT"
    compare_001.mode = "ELEMENT"
    compare_001.operation = "EQUAL"
    # B
    compare_001.inputs[1].default_value = -1.0
    # Epsilon
    compare_001.inputs[12].default_value = 0.0010000000474974513

    # node Mesh Boolean
    mesh_boolean = lunarrock.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = "DIFFERENCE"
    mesh_boolean.solver = "FLOAT"
    # Self Intersection
    mesh_boolean.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean.inputs[3].default_value = False

    # node Switch
    switch_1 = lunarrock.nodes.new("GeometryNodeSwitch")
    switch_1.name = "Switch"
    switch_1.input_type = "GEOMETRY"

    # node Transform Geometry.002
    transform_geometry_002 = lunarrock.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = "COMPONENTS"
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    transform_geometry_002.inputs[4].hide = True
    # Rotation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Combine XYZ
    combine_xyz = lunarrock.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    # X
    combine_xyz.inputs[0].default_value = 0.0
    # Y
    combine_xyz.inputs[1].default_value = 0.0

    # node Reroute.010
    reroute_010 = lunarrock.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.socket_idname = "NodeSocketBool"
    # node Cube.001
    cube_001 = lunarrock.nodes.new("GeometryNodeMeshCube")
    cube_001.name = "Cube.001"
    # Size
    cube_001.inputs[0].default_value = (2.0, 2.0, 2.0)
    # Vertices X
    cube_001.inputs[1].default_value = 2
    # Vertices Y
    cube_001.inputs[2].default_value = 2
    # Vertices Z
    cube_001.inputs[3].default_value = 2

    # node Math
    math_1 = lunarrock.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = "SUBTRACT"
    math_1.use_clamp = False
    # Value_001
    math_1.inputs[1].default_value = 1.0

    # node Reroute.004
    reroute_004 = lunarrock.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketGeometry"
    # node Frame.004
    frame_004 = lunarrock.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    # node Reroute.012
    reroute_012 = lunarrock.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.socket_idname = "NodeSocketFloatDistance"
    # node Reroute.013
    reroute_013 = lunarrock.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.socket_idname = "NodeSocketFloatDistance"
    # node Transform Geometry.003
    transform_geometry_003 = lunarrock.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = "COMPONENTS"
    transform_geometry_003.inputs[1].hide = True
    transform_geometry_003.inputs[2].hide = True
    transform_geometry_003.inputs[4].hide = True
    # Translation
    transform_geometry_003.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Combine XYZ.001
    combine_xyz_001 = lunarrock.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"

    # node Group.009
    group_009 = lunarrock.nodes.new("GeometryNodeGroup")
    group_009.name = "Group.009"
    group_009.node_tree = random__normal_
    # Socket_1
    group_009.inputs[0].default_value = True
    # Socket_5
    group_009.inputs[4].default_value = 31680

    # node Group.013
    group_013 = lunarrock.nodes.new("GeometryNodeGroup")
    group_013.name = "Group.013"
    group_013.node_tree = random__normal_
    # Socket_1
    group_013.inputs[0].default_value = True
    # Socket_5
    group_013.inputs[4].default_value = 32260

    # node Group.014
    group_014 = lunarrock.nodes.new("GeometryNodeGroup")
    group_014.name = "Group.014"
    group_014.node_tree = random__normal_
    # Socket_1
    group_014.inputs[0].default_value = True
    # Socket_5
    group_014.inputs[4].default_value = 40590

    # node Reroute.015
    reroute_015 = lunarrock.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.socket_idname = "NodeSocketFloat"
    # node Separate XYZ
    separate_xyz = lunarrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    # node Separate XYZ.003
    separate_xyz_003 = lunarrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"

    # node Reroute.017
    reroute_017 = lunarrock.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.socket_idname = "NodeSocketVectorXYZ"
    # node Reroute.018
    reroute_018 = lunarrock.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.socket_idname = "NodeSocketVectorXYZ"
    # node Reroute.019
    reroute_019 = lunarrock.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.socket_idname = "NodeSocketVectorXYZ"
    # node Reroute.020
    reroute_020 = lunarrock.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.socket_idname = "NodeSocketFloat"
    # node Reroute.021
    reroute_021 = lunarrock.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    reroute_021.socket_idname = "NodeSocketBool"
    # node Reroute.022
    reroute_022 = lunarrock.nodes.new("NodeReroute")
    reroute_022.name = "Reroute.022"
    reroute_022.socket_idname = "NodeSocketFloatDistance"
    # node Frame.005
    frame_005 = lunarrock.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    # node Math.001
    math_001_1 = lunarrock.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = "ADD"
    math_001_1.use_clamp = False

    # node Integer.001
    integer_001 = lunarrock.nodes.new("FunctionNodeInputInt")
    integer_001.label = "Global Seed Offset"
    integer_001.name = "Integer.001"
    integer_001.integer = 0

    # Set parents
    cube.parent = frame_002
    subdivision_surface.parent = frame_002
    set_position.parent = frame_1
    voronoi_texture.parent = frame_1
    vector_math.parent = frame_1
    position.parent = frame_1
    map_range.parent = frame_1
    set_position_001.parent = frame_001_1
    vector_math_001.parent = frame_001_1
    position_001.parent = frame_001_1
    noise_texture.parent = frame_001_1
    reroute_001.parent = frame_001_1
    transform_geometry.parent = frame_003_1
    reroute_002.parent = frame_002
    attribute_statistic.parent = frame_003_1
    position_002.parent = frame_003_1
    reroute_003.parent = frame_003_1
    vector_math_002.parent = frame_003_1
    vector_math_003.parent = frame_003_1
    vector_math_004.parent = frame_003_1
    group.parent = frame_1
    group_001.parent = frame_1
    group_002.parent = frame_1
    group_004.parent = frame_1
    float_curve.parent = frame_1
    group_005.parent = frame_1
    reroute_005.parent = frame_1
    group_003.parent = frame_002
    group_006.parent = frame_002
    reroute_006.parent = frame_002
    group_007.parent = frame_001_1
    group_008.parent = frame_001_1
    group_010.parent = frame_001_1
    group_011.parent = frame_001_1
    group_012.parent = frame_001_1
    transform_geometry_001.parent = frame_002
    random_value.parent = frame_002
    integer.parent = frame_002
    delete_geometry.parent = frame_004
    compare.parent = frame_004
    position_004.parent = frame_004
    separate_xyz_001.parent = frame_004
    normal_001.parent = frame_004
    boolean_math.parent = frame_004
    separate_xyz_002.parent = frame_004
    compare_001.parent = frame_004
    mesh_boolean.parent = frame_004
    switch_1.parent = frame_004
    transform_geometry_002.parent = frame_004
    combine_xyz.parent = frame_004
    cube_001.parent = frame_004
    math_1.parent = frame_004
    reroute_004.parent = frame_004
    reroute_012.parent = frame_004
    transform_geometry_003.parent = frame_005
    combine_xyz_001.parent = frame_005
    group_009.parent = frame_005
    group_013.parent = frame_005
    group_014.parent = frame_005
    separate_xyz.parent = frame_005
    separate_xyz_003.parent = frame_005

    # Set locations
    group_input_2.location = (-4957.7626953125, -82.99918365478516)
    group_output_2.location = (2629.999755859375, 0.0)
    set_material.location = (2439.999755859375, 23.5)
    cube.location = (-1513.1207275390625, 915.7615966796875)
    subdivision_surface.location = (-340.2048034667969, 1023.5044555664062)
    set_position.location = (726.622314453125, 908.64501953125)
    voronoi_texture.location = (-133.37771606445312, 678.8929443359375)
    vector_math.location = (536.622314453125, 703.8929443359375)
    position.location = (346.6222839355469, 666.3929443359375)
    map_range.location = (346.6222839355469, 601.3929443359375)
    set_position_001.location = (1584.2333984375, 260.2159423828125)
    vector_math_001.location = (1394.2333984375, 108.06204986572266)
    position_001.location = (1204.2333984375, 70.56206512451172)
    noise_texture.location = (1001.9918212890625, 32.7781982421875)
    set_shade_smooth.location = (2249.999755859375, 35.5)
    frame_1.location = (-2794.595703125, 186.608642578125)
    frame_001_1.location = (-3649.0771484375, -318.5823059082031)
    frame_002.location = (-3290.830078125, 71.48291015625)
    reroute_001.location = (666.5570068359375, -219.35711669921875)
    transform_geometry.location = (1809.3837890625, -34.2188835144043)
    reroute_002.location = (-688.463623046875, 896.0345458984375)
    attribute_statistic.location = (1183.53466796875, -268.6141662597656)
    position_002.location = (993.53466796875, -339.6141662597656)
    reroute_003.location = (1086.59716796875, -128.1580352783203)
    vector_math_002.location = (1373.53466796875, -337.17041015625)
    vector_math_003.location = (1373.53466796875, -197.17041015625)
    vector_math_004.location = (1563.53466796875, -198.17041015625)
    group.location = (-434.4251708984375, 622.037353515625)
    group_001.location = (-434.4251708984375, 800.037353515625)
    group_002.location = (-434.4251708984375, 422.037353515625)
    group_004.location = (-434.4251708984375, 22.037353515625)
    float_curve.location = (56.622283935546875, 636.3929443359375)
    group_005.location = (-434.4251708984375, 222.037353515625)
    reroute_005.location = (-594.6759643554688, 278.4246826171875)
    group_003.location = (-654.701904296875, 678.068603515625)
    group_006.location = (-654.701904296875, 878.068603515625)
    reroute_006.location = (-694.4317626953125, 732.759765625)
    reroute.location = (-3415.009765625, -1250.500732421875)
    group_007.location = (733.760498046875, 245.83392333984375)
    group_008.location = (733.760498046875, 67.83392333984375)
    group_010.location = (733.760498046875, -132.16607666015625)
    group_011.location = (733.760498046875, -332.16607666015625)
    group_012.location = (733.760498046875, -532.1660766601562)
    frame_003_1.location = (-2665.356201171875, 28.966693878173828)
    transform_geometry_001.location = (-943.1207275390625, 961.654052734375)
    random_value.location = (-1133.1207275390625, 838.7128295898438)
    integer.location = (-1323.1207275390625, 816.7128295898438)
    delete_geometry.location = (1346.2703857421875, -536.0291137695312)
    compare.location = (966.2703857421875, -950.8118896484375)
    position_004.location = (586.2703857421875, -1009.8118896484375)
    separate_xyz_001.location = (776.2703857421875, -997.3118896484375)
    normal_001.location = (586.2703857421875, -828.6788330078125)
    boolean_math.location = (1156.2703857421875, -769.6106567382812)
    separate_xyz_002.location = (776.2703857421875, -816.1788330078125)
    compare_001.location = (966.2703857421875, -769.6788330078125)
    mesh_boolean.location = (965.2637939453125, -511.6483154296875)
    switch_1.location = (1665.2486572265625, -268.939453125)
    transform_geometry_002.location = (775.2637939453125, -585.58447265625)
    combine_xyz.location = (585.2637939453125, -656.6286010742188)
    reroute_010.location = (-3415.009765625, -1287.8094482421875)
    cube_001.location = (395.2638244628906, -535.58447265625)
    math_1.location = (395.2638244628906, -773.58447265625)
    reroute_004.location = (702.1375732421875, -330.8438720703125)
    frame_004.location = (-904.48779296875, 272.091064453125)
    reroute_012.location = (368.2854309082031, -1095.044189453125)
    reroute_013.location = (-3415.009765625, -1303.5126953125)
    transform_geometry_003.location = (1706.2198486328125, -32.31362533569336)
    combine_xyz_001.location = (1538.015380859375, -398.0220642089844)
    group_009.location = (1308.17041015625, -245.8809814453125)
    group_013.location = (1308.17041015625, -445.8809814453125)
    group_014.location = (1308.17041015625, -645.8809814453125)
    reroute_015.location = (-3415.009765625, -1234.2786865234375)
    separate_xyz.location = (949.9049682617188, -448.3955383300781)
    separate_xyz_003.location = (949.9049682617188, -582.3955078125)
    reroute_017.location = (-3415.009765625, -1270.66552734375)
    reroute_018.location = (871.9225463867188, -1251.0347900390625)
    reroute_019.location = (871.9225463867188, -1271.1376953125)
    reroute_020.location = (1295.392578125, -1234.255126953125)
    reroute_021.location = (559.1981201171875, -1287.5440673828125)
    reroute_022.location = (-1005.0067138671875, -1303.1754150390625)
    frame_005.location = (145.8409423828125, 25.487651824951172)
    math_001_1.location = (-4690.5810546875, -4.762271881103516)
    integer_001.location = (-4956.11669921875, 50.9406852722168)

    # initialize lunarrock links
    # set_material.Geometry -> group_output_2.Geometry
    lunarrock.links.new(set_material.outputs[0], group_output_2.inputs[0])
    # set_shade_smooth.Geometry -> set_material.Geometry
    lunarrock.links.new(set_shade_smooth.outputs[0], set_material.inputs[0])
    # reroute_002.Output -> subdivision_surface.Level
    lunarrock.links.new(reroute_002.outputs[0], subdivision_surface.inputs[1])
    # position.Position -> vector_math.Vector
    lunarrock.links.new(position.outputs[0], vector_math.inputs[0])
    # map_range.Result -> vector_math.Vector
    lunarrock.links.new(map_range.outputs[0], vector_math.inputs[1])
    # vector_math.Vector -> set_position.Position
    lunarrock.links.new(vector_math.outputs[0], set_position.inputs[2])
    # position_001.Position -> vector_math_001.Vector
    lunarrock.links.new(position_001.outputs[0], vector_math_001.inputs[0])
    # noise_texture.Fac -> vector_math_001.Vector
    lunarrock.links.new(noise_texture.outputs[0], vector_math_001.inputs[1])
    # reroute_003.Output -> transform_geometry.Geometry
    lunarrock.links.new(reroute_003.outputs[0], transform_geometry.inputs[0])
    # math_001_1.Value -> reroute_001.Input
    lunarrock.links.new(math_001_1.outputs[0], reroute_001.inputs[0])
    # position_002.Position -> attribute_statistic.Attribute
    lunarrock.links.new(position_002.outputs[0], attribute_statistic.inputs[2])
    # set_position_001.Geometry -> reroute_003.Input
    lunarrock.links.new(set_position_001.outputs[0], reroute_003.inputs[0])
    # reroute_003.Output -> attribute_statistic.Geometry
    lunarrock.links.new(reroute_003.outputs[0], attribute_statistic.inputs[0])
    # vector_math_002.Vector -> transform_geometry.Scale
    lunarrock.links.new(vector_math_002.outputs[0], transform_geometry.inputs[3])
    # attribute_statistic.Range -> vector_math_002.Vector
    lunarrock.links.new(attribute_statistic.outputs[5], vector_math_002.inputs[1])
    # vector_math_004.Vector -> transform_geometry.Translation
    lunarrock.links.new(vector_math_004.outputs[0], transform_geometry.inputs[1])
    # vector_math_003.Vector -> vector_math_004.Vector
    lunarrock.links.new(vector_math_003.outputs[0], vector_math_004.inputs[0])
    # attribute_statistic.Min -> vector_math_003.Vector
    lunarrock.links.new(attribute_statistic.outputs[3], vector_math_003.inputs[0])
    # attribute_statistic.Max -> vector_math_003.Vector
    lunarrock.links.new(attribute_statistic.outputs[4], vector_math_003.inputs[1])
    # group_001.Value -> voronoi_texture.W
    lunarrock.links.new(group_001.outputs[0], voronoi_texture.inputs[1])
    # reroute_005.Output -> group_001.Seed
    lunarrock.links.new(reroute_005.outputs[0], group_001.inputs[2])
    # group.Value -> voronoi_texture.Scale
    lunarrock.links.new(group.outputs[0], voronoi_texture.inputs[2])
    # group_002.Value -> voronoi_texture.Detail
    lunarrock.links.new(group_002.outputs[0], voronoi_texture.inputs[3])
    # group_004.Value -> voronoi_texture.Lacunarity
    lunarrock.links.new(group_004.outputs[0], voronoi_texture.inputs[5])
    # reroute_005.Output -> group.Seed
    lunarrock.links.new(reroute_005.outputs[0], group.inputs[3])
    # reroute_005.Output -> group_002.Seed
    lunarrock.links.new(reroute_005.outputs[0], group_002.inputs[3])
    # reroute_005.Output -> group_004.Seed
    lunarrock.links.new(reroute_005.outputs[0], group_004.inputs[3])
    # subdivision_surface.Mesh -> set_position.Geometry
    lunarrock.links.new(subdivision_surface.outputs[0], set_position.inputs[0])
    # set_position.Geometry -> set_position_001.Geometry
    lunarrock.links.new(set_position.outputs[0], set_position_001.inputs[0])
    # float_curve.Value -> map_range.Value
    lunarrock.links.new(float_curve.outputs[0], map_range.inputs[0])
    # voronoi_texture.Distance -> float_curve.Value
    lunarrock.links.new(voronoi_texture.outputs[0], float_curve.inputs[1])
    # reroute_005.Output -> group_005.Seed
    lunarrock.links.new(reroute_005.outputs[0], group_005.inputs[3])
    # group_005.Value -> voronoi_texture.Roughness
    lunarrock.links.new(group_005.outputs[0], voronoi_texture.inputs[4])
    # math_001_1.Value -> reroute_005.Input
    lunarrock.links.new(math_001_1.outputs[0], reroute_005.inputs[0])
    # reroute_006.Output -> group_003.Seed
    lunarrock.links.new(reroute_006.outputs[0], group_003.inputs[3])
    # reroute_006.Output -> group_006.Seed
    lunarrock.links.new(reroute_006.outputs[0], group_006.inputs[3])
    # group_003.Value -> subdivision_surface.Vertex Crease
    lunarrock.links.new(group_003.outputs[0], subdivision_surface.inputs[3])
    # group_006.Value -> subdivision_surface.Edge Crease
    lunarrock.links.new(group_006.outputs[0], subdivision_surface.inputs[2])
    # math_001_1.Value -> reroute_006.Input
    lunarrock.links.new(math_001_1.outputs[0], reroute_006.inputs[0])
    # group_input_2.Scale -> reroute.Input
    lunarrock.links.new(group_input_2.outputs[2], reroute.inputs[0])
    # group_input_2.Subdivisions -> reroute_002.Input
    lunarrock.links.new(group_input_2.outputs[1], reroute_002.inputs[0])
    # vector_math_001.Vector -> set_position_001.Position
    lunarrock.links.new(vector_math_001.outputs[0], set_position_001.inputs[2])
    # reroute_001.Output -> group_007.Seed
    lunarrock.links.new(reroute_001.outputs[0], group_007.inputs[2])
    # group_007.Value -> noise_texture.W
    lunarrock.links.new(group_007.outputs[0], noise_texture.inputs[1])
    # reroute_001.Output -> group_008.Seed
    lunarrock.links.new(reroute_001.outputs[0], group_008.inputs[3])
    # reroute_001.Output -> group_010.Seed
    lunarrock.links.new(reroute_001.outputs[0], group_010.inputs[3])
    # reroute_001.Output -> group_011.Seed
    lunarrock.links.new(reroute_001.outputs[0], group_011.inputs[3])
    # reroute_001.Output -> group_012.Seed
    lunarrock.links.new(reroute_001.outputs[0], group_012.inputs[3])
    # group_012.Value -> noise_texture.Distortion
    lunarrock.links.new(group_012.outputs[0], noise_texture.inputs[8])
    # group_010.Value -> noise_texture.Roughness
    lunarrock.links.new(group_010.outputs[0], noise_texture.inputs[4])
    # group_011.Value -> noise_texture.Lacunarity
    lunarrock.links.new(group_011.outputs[0], noise_texture.inputs[5])
    # group_008.Value -> noise_texture.Scale
    lunarrock.links.new(group_008.outputs[0], noise_texture.inputs[2])
    # integer.Integer -> random_value.ID
    lunarrock.links.new(integer.outputs[0], random_value.inputs[7])
    # random_value.Value -> transform_geometry_001.Rotation
    lunarrock.links.new(random_value.outputs[0], transform_geometry_001.inputs[2])
    # transform_geometry_001.Geometry -> subdivision_surface.Mesh
    lunarrock.links.new(
        transform_geometry_001.outputs[0], subdivision_surface.inputs[0]
    )
    # cube.Mesh -> transform_geometry_001.Geometry
    lunarrock.links.new(cube.outputs[0], transform_geometry_001.inputs[0])
    # math_001_1.Value -> random_value.Seed
    lunarrock.links.new(math_001_1.outputs[0], random_value.inputs[8])
    # mesh_boolean.Mesh -> delete_geometry.Geometry
    lunarrock.links.new(mesh_boolean.outputs[0], delete_geometry.inputs[0])
    # position_004.Position -> compare.A
    lunarrock.links.new(position_004.outputs[0], compare.inputs[4])
    # separate_xyz_001.Z -> compare.A
    lunarrock.links.new(separate_xyz_001.outputs[2], compare.inputs[0])
    # normal_001.Normal -> separate_xyz_002.Vector
    lunarrock.links.new(normal_001.outputs[0], separate_xyz_002.inputs[0])
    # separate_xyz_002.Z -> compare_001.A
    lunarrock.links.new(separate_xyz_002.outputs[2], compare_001.inputs[0])
    # boolean_math.Boolean -> delete_geometry.Selection
    lunarrock.links.new(boolean_math.outputs[0], delete_geometry.inputs[1])
    # reroute_004.Output -> mesh_boolean.Mesh 1
    lunarrock.links.new(reroute_004.outputs[0], mesh_boolean.inputs[0])
    # transform_geometry_002.Geometry -> mesh_boolean.Mesh 2
    lunarrock.links.new(transform_geometry_002.outputs[0], mesh_boolean.inputs[1])
    # position_004.Position -> separate_xyz_001.Vector
    lunarrock.links.new(position_004.outputs[0], separate_xyz_001.inputs[0])
    # reroute_021.Output -> switch_1.Switch
    lunarrock.links.new(reroute_021.outputs[0], switch_1.inputs[0])
    # transform_geometry_003.Geometry -> set_shade_smooth.Geometry
    lunarrock.links.new(transform_geometry_003.outputs[0], set_shade_smooth.inputs[0])
    # reroute_004.Output -> switch_1.False
    lunarrock.links.new(reroute_004.outputs[0], switch_1.inputs[1])
    # delete_geometry.Geometry -> switch_1.True
    lunarrock.links.new(delete_geometry.outputs[0], switch_1.inputs[2])
    # math_1.Value -> combine_xyz.Z
    lunarrock.links.new(math_1.outputs[0], combine_xyz.inputs[2])
    # reroute_012.Output -> compare.B
    lunarrock.links.new(reroute_012.outputs[0], compare.inputs[1])
    # group_input_2.Horizontal Cut -> reroute_010.Input
    lunarrock.links.new(group_input_2.outputs[4], reroute_010.inputs[0])
    # compare_001.Result -> boolean_math.Boolean
    lunarrock.links.new(compare_001.outputs[0], boolean_math.inputs[0])
    # compare.Result -> boolean_math.Boolean
    lunarrock.links.new(compare.outputs[0], boolean_math.inputs[1])
    # cube_001.Mesh -> transform_geometry_002.Geometry
    lunarrock.links.new(cube_001.outputs[0], transform_geometry_002.inputs[0])
    # combine_xyz.Vector -> transform_geometry_002.Translation
    lunarrock.links.new(combine_xyz.outputs[0], transform_geometry_002.inputs[1])
    # reroute_012.Output -> math_1.Value
    lunarrock.links.new(reroute_012.outputs[0], math_1.inputs[0])
    # transform_geometry.Geometry -> reroute_004.Input
    lunarrock.links.new(transform_geometry.outputs[0], reroute_004.inputs[0])
    # reroute_022.Output -> reroute_012.Input
    lunarrock.links.new(reroute_022.outputs[0], reroute_012.inputs[0])
    # group_input_2.Horizontal Cut Offset -> reroute_013.Input
    lunarrock.links.new(group_input_2.outputs[5], reroute_013.inputs[0])
    # switch_1.Output -> transform_geometry_003.Geometry
    lunarrock.links.new(switch_1.outputs[0], transform_geometry_003.inputs[0])
    # group_009.Value -> combine_xyz_001.X
    lunarrock.links.new(group_009.outputs[0], combine_xyz_001.inputs[0])
    # group_013.Value -> combine_xyz_001.Y
    lunarrock.links.new(group_013.outputs[0], combine_xyz_001.inputs[1])
    # group_014.Value -> combine_xyz_001.Z
    lunarrock.links.new(group_014.outputs[0], combine_xyz_001.inputs[2])
    # combine_xyz_001.Vector -> transform_geometry_003.Scale
    lunarrock.links.new(combine_xyz_001.outputs[0], transform_geometry_003.inputs[3])
    # math_001_1.Value -> reroute_015.Input
    lunarrock.links.new(math_001_1.outputs[0], reroute_015.inputs[0])
    # reroute_020.Output -> group_013.Seed
    lunarrock.links.new(reroute_020.outputs[0], group_013.inputs[3])
    # reroute_020.Output -> group_009.Seed
    lunarrock.links.new(reroute_020.outputs[0], group_009.inputs[3])
    # reroute_020.Output -> group_014.Seed
    lunarrock.links.new(reroute_020.outputs[0], group_014.inputs[3])
    # reroute_019.Output -> separate_xyz_003.Vector
    lunarrock.links.new(reroute_019.outputs[0], separate_xyz_003.inputs[0])
    # separate_xyz_003.X -> group_009.Std. Dev.
    lunarrock.links.new(separate_xyz_003.outputs[0], group_009.inputs[2])
    # separate_xyz_003.Y -> group_013.Std. Dev.
    lunarrock.links.new(separate_xyz_003.outputs[1], group_013.inputs[2])
    # separate_xyz_003.Z -> group_014.Std. Dev.
    lunarrock.links.new(separate_xyz_003.outputs[2], group_014.inputs[2])
    # separate_xyz.X -> group_009.Mean
    lunarrock.links.new(separate_xyz.outputs[0], group_009.inputs[1])
    # separate_xyz.Y -> group_013.Mean
    lunarrock.links.new(separate_xyz.outputs[1], group_013.inputs[1])
    # separate_xyz.Z -> group_014.Mean
    lunarrock.links.new(separate_xyz.outputs[2], group_014.inputs[1])
    # reroute_018.Output -> separate_xyz.Vector
    lunarrock.links.new(reroute_018.outputs[0], separate_xyz.inputs[0])
    # group_input_2.Scale STD -> reroute_017.Input
    lunarrock.links.new(group_input_2.outputs[3], reroute_017.inputs[0])
    # reroute.Output -> reroute_018.Input
    lunarrock.links.new(reroute.outputs[0], reroute_018.inputs[0])
    # reroute_017.Output -> reroute_019.Input
    lunarrock.links.new(reroute_017.outputs[0], reroute_019.inputs[0])
    # reroute_015.Output -> reroute_020.Input
    lunarrock.links.new(reroute_015.outputs[0], reroute_020.inputs[0])
    # reroute_010.Output -> reroute_021.Input
    lunarrock.links.new(reroute_010.outputs[0], reroute_021.inputs[0])
    # reroute_013.Output -> reroute_022.Input
    lunarrock.links.new(reroute_013.outputs[0], reroute_022.inputs[0])
    # group_input_2.Seed -> math_001_1.Value
    lunarrock.links.new(group_input_2.outputs[0], math_001_1.inputs[0])
    # integer_001.Integer -> math_001_1.Value
    lunarrock.links.new(integer_001.outputs[0], math_001_1.inputs[1])
    return lunarrock


lunarrock = lunarrock_node_group()
