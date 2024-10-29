import bpy


# initialize blankmodule node group
def blankmodule_node_group():
    blankmodule = bpy.data.node_groups.new(type="GeometryNodeTree", name="BlankModule")

    blankmodule.color_tag = "NONE"
    blankmodule.description = ""

    blankmodule.is_modifier = True

    # blankmodule interface
    # Socket Geometry
    geometry_socket = blankmodule.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket.attribute_domain = "POINT"

    # Socket module_centering
    module_centering_socket = blankmodule.interface.new_socket(
        name="module_centering", in_out="INPUT", socket_type="NodeSocketBool"
    )
    module_centering_socket.default_value = True
    module_centering_socket.attribute_domain = "POINT"

    # Socket module_size
    module_size_socket = blankmodule.interface.new_socket(
        name="module_size", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    module_size_socket.default_value = 0.15000000596046448
    module_size_socket.min_value = 0.0
    module_size_socket.max_value = 3.4028234663852886e38
    module_size_socket.subtype = "DISTANCE"
    module_size_socket.attribute_domain = "POINT"
    module_size_socket.description = "Size of a single square module in the XY plane"

    # Socket module_thickness
    module_thickness_socket = blankmodule.interface.new_socket(
        name="module_thickness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    module_thickness_socket.default_value = 0.20000000298023224
    module_thickness_socket.min_value = 0.0
    module_thickness_socket.max_value = 3.4028234663852886e38
    module_thickness_socket.subtype = "DISTANCE"
    module_thickness_socket.attribute_domain = "POINT"
    module_thickness_socket.description = "Thickness of module along Z axis"

    # Socket module_size_tolerance
    module_size_tolerance_socket = blankmodule.interface.new_socket(
        name="module_size_tolerance", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    module_size_tolerance_socket.default_value = 0.0
    module_size_tolerance_socket.min_value = 0.0
    module_size_tolerance_socket.max_value = 3.4028234663852886e38
    module_size_tolerance_socket.subtype = "DISTANCE"
    module_size_tolerance_socket.attribute_domain = "POINT"

    # Socket module_count_x
    module_count_x_socket = blankmodule.interface.new_socket(
        name="module_count_x", in_out="INPUT", socket_type="NodeSocketInt"
    )
    module_count_x_socket.default_value = 1
    module_count_x_socket.min_value = 1
    module_count_x_socket.max_value = 2147483647
    module_count_x_socket.subtype = "NONE"
    module_count_x_socket.attribute_domain = "POINT"
    module_count_x_socket.description = "Number of combined module plates along X axis"

    # Socket module_count_y
    module_count_y_socket = blankmodule.interface.new_socket(
        name="module_count_y", in_out="INPUT", socket_type="NodeSocketInt"
    )
    module_count_y_socket.default_value = 1
    module_count_y_socket.min_value = 1
    module_count_y_socket.max_value = 2147483647
    module_count_y_socket.subtype = "NONE"
    module_count_y_socket.attribute_domain = "POINT"
    module_count_y_socket.description = "Number of combined module plates along Y axis"

    # Socket holes_enable
    holes_enable_socket = blankmodule.interface.new_socket(
        name="holes_enable", in_out="INPUT", socket_type="NodeSocketBool"
    )
    holes_enable_socket.default_value = False
    holes_enable_socket.attribute_domain = "POINT"

    # Socket holes_vertices
    holes_vertices_socket = blankmodule.interface.new_socket(
        name="holes_vertices", in_out="INPUT", socket_type="NodeSocketInt"
    )
    holes_vertices_socket.default_value = 16
    holes_vertices_socket.min_value = 3
    holes_vertices_socket.max_value = 2147483647
    holes_vertices_socket.subtype = "NONE"
    holes_vertices_socket.attribute_domain = "POINT"

    # Socket holes_offset_from_corner
    holes_offset_from_corner_socket = blankmodule.interface.new_socket(
        name="holes_offset_from_corner", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    holes_offset_from_corner_socket.default_value = 0.014999999664723873
    holes_offset_from_corner_socket.min_value = 0.0
    holes_offset_from_corner_socket.max_value = 3.4028234663852886e38
    holes_offset_from_corner_socket.subtype = "DISTANCE"
    holes_offset_from_corner_socket.attribute_domain = "POINT"

    # Socket holes_diameter
    holes_diameter_socket = blankmodule.interface.new_socket(
        name="holes_diameter", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    holes_diameter_socket.default_value = 0.00430000014603138
    holes_diameter_socket.min_value = 0.0
    holes_diameter_socket.max_value = 3.4028234663852886e38
    holes_diameter_socket.subtype = "DISTANCE"
    holes_diameter_socket.attribute_domain = "POINT"

    # initialize blankmodule nodes
    # node Frame
    frame = blankmodule.nodes.new("NodeFrame")
    frame.label = "Module (1x1)"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # node Frame.001
    frame_001 = blankmodule.nodes.new("NodeFrame")
    frame_001.label = "Extend to MxN modules"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # node Frame.002
    frame_002 = blankmodule.nodes.new("NodeFrame")
    frame_002.label = "Tolerance (reduce module size in XY plane)"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # node Frame.003
    frame_003 = blankmodule.nodes.new("NodeFrame")
    frame_003.label = "Holes (if enabled)"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # node Frame.004
    frame_004 = blankmodule.nodes.new("NodeFrame")
    frame_004.label = "Set origin to module centre (if enabled)"
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    # node Frame.005
    frame_005 = blankmodule.nodes.new("NodeFrame")
    frame_005.label = "Set origin to the bottom of the module"
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    # node Transform Geometry
    transform_geometry = blankmodule.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = "COMPONENTS"
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[3].hide = True
    # Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Group Input
    group_input = blankmodule.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[0].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True
    group_input.outputs[6].hide = True
    group_input.outputs[7].hide = True
    group_input.outputs[8].hide = True
    group_input.outputs[9].hide = True
    group_input.outputs[10].hide = True

    # node Cube
    cube = blankmodule.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    # Vertices X
    cube.inputs[1].default_value = 2
    # Vertices Y
    cube.inputs[2].default_value = 2
    # Vertices Z
    cube.inputs[3].default_value = 2

    # node Combine XYZ
    combine_xyz = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"

    # node Combine XYZ.001
    combine_xyz_001 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.inputs[2].hide = True
    # Z
    combine_xyz_001.inputs[2].default_value = 0.0

    # node Group Input.001
    group_input_001 = blankmodule.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True
    group_input_001.outputs[7].hide = True
    group_input_001.outputs[8].hide = True
    group_input_001.outputs[9].hide = True
    group_input_001.outputs[10].hide = True

    # node Math
    math = blankmodule.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = "MULTIPLY"
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 0.5

    # node Normal
    normal = blankmodule.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"

    # node Separate XYZ
    separate_xyz = blankmodule.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.outputs[2].hide = True

    # node Compare
    compare = blankmodule.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = "FLOAT"
    compare.mode = "ELEMENT"
    compare.operation = "GREATER_THAN"
    # B
    compare.inputs[1].default_value = 0.0

    # node Group Input.002
    group_input_002 = blankmodule.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[2].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True
    group_input_002.outputs[8].hide = True
    group_input_002.outputs[9].hide = True
    group_input_002.outputs[10].hide = True

    # node Math.001
    math_001 = blankmodule.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = "ADD"
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = -1.0

    # node Combine XYZ.002
    combine_xyz_002 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.inputs[0].hide = True
    combine_xyz_002.inputs[2].hide = True
    # X
    combine_xyz_002.inputs[0].default_value = 0.0
    # Z
    combine_xyz_002.inputs[2].default_value = 0.0

    # node Math.002
    math_002 = blankmodule.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = "MULTIPLY"
    math_002.use_clamp = False
    math_002.inputs[2].hide = True

    # node Math.003
    math_003 = blankmodule.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = "MULTIPLY"
    math_003.use_clamp = False

    # node Math.004
    math_004 = blankmodule.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = "ADD"
    math_004.use_clamp = False
    # Value_001
    math_004.inputs[1].default_value = -1.0

    # node Group Input.003
    group_input_003 = blankmodule.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[10].hide = True

    # node Combine XYZ.003
    combine_xyz_003 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    combine_xyz_003.inputs[1].hide = True
    combine_xyz_003.inputs[2].hide = True
    # Y
    combine_xyz_003.inputs[1].default_value = 0.0
    # Z
    combine_xyz_003.inputs[2].default_value = 0.0

    # node Compare.001
    compare_001 = blankmodule.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = "FLOAT"
    compare_001.mode = "ELEMENT"
    compare_001.operation = "GREATER_THAN"
    # B
    compare_001.inputs[1].default_value = 0.0

    # node Set Position
    set_position = blankmodule.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    # Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Set Position.001
    set_position_001 = blankmodule.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    # Position
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Set Position.002
    set_position_002 = blankmodule.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    # Position
    set_position_002.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Set Position.003
    set_position_003 = blankmodule.nodes.new("GeometryNodeSetPosition")
    set_position_003.name = "Set Position.003"
    # Position
    set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Combine XYZ.004
    combine_xyz_004 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    combine_xyz_004.inputs[0].hide = True
    combine_xyz_004.inputs[2].hide = True
    # X
    combine_xyz_004.inputs[0].default_value = 0.0
    # Z
    combine_xyz_004.inputs[2].default_value = 0.0

    # node Combine XYZ.005
    combine_xyz_005 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"
    combine_xyz_005.inputs[0].hide = True
    combine_xyz_005.inputs[2].hide = True
    # X
    combine_xyz_005.inputs[0].default_value = 0.0
    # Z
    combine_xyz_005.inputs[2].default_value = 0.0

    # node Math.005
    math_005 = blankmodule.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = "MULTIPLY"
    math_005.use_clamp = False
    # Value_001
    math_005.inputs[1].default_value = -1.0

    # node Group Input.004
    group_input_004 = blankmodule.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True

    # node Compare.002
    compare_002 = blankmodule.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = "FLOAT"
    compare_002.mode = "ELEMENT"
    compare_002.operation = "GREATER_THAN"
    # B
    compare_002.inputs[1].default_value = 0.0

    # node Compare.003
    compare_003 = blankmodule.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = "FLOAT"
    compare_003.mode = "ELEMENT"
    compare_003.operation = "LESS_THAN"
    # B
    compare_003.inputs[1].default_value = 0.0

    # node Separate XYZ.001
    separate_xyz_001 = blankmodule.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.outputs[0].hide = True
    separate_xyz_001.outputs[2].hide = True

    # node Normal.001
    normal_001 = blankmodule.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"

    # node Separate XYZ.002
    separate_xyz_002 = blankmodule.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"
    separate_xyz_002.outputs[1].hide = True
    separate_xyz_002.outputs[2].hide = True

    # node Compare.004
    compare_004 = blankmodule.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = "FLOAT"
    compare_004.mode = "ELEMENT"
    compare_004.operation = "LESS_THAN"
    # B
    compare_004.inputs[1].default_value = 0.0

    # node Compare.005
    compare_005 = blankmodule.nodes.new("FunctionNodeCompare")
    compare_005.name = "Compare.005"
    compare_005.data_type = "FLOAT"
    compare_005.mode = "ELEMENT"
    compare_005.operation = "GREATER_THAN"
    # B
    compare_005.inputs[1].default_value = 0.0

    # node Group Input.005
    group_input_005 = blankmodule.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[6].hide = True
    group_input_005.outputs[7].hide = True
    group_input_005.outputs[8].hide = True
    group_input_005.outputs[9].hide = True
    group_input_005.outputs[10].hide = True

    # node Math.006
    math_006 = blankmodule.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = "MULTIPLY"
    math_006.use_clamp = False
    # Value_001
    math_006.inputs[1].default_value = -1.0

    # node Combine XYZ.006
    combine_xyz_006 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    combine_xyz_006.inputs[1].hide = True
    combine_xyz_006.inputs[2].hide = True
    # Y
    combine_xyz_006.inputs[1].default_value = 0.0
    # Z
    combine_xyz_006.inputs[2].default_value = 0.0

    # node Combine XYZ.007
    combine_xyz_007 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_007.name = "Combine XYZ.007"
    combine_xyz_007.inputs[1].hide = True
    combine_xyz_007.inputs[2].hide = True
    # Y
    combine_xyz_007.inputs[1].default_value = 0.0
    # Z
    combine_xyz_007.inputs[2].default_value = 0.0

    # node Set Position.004
    set_position_004 = blankmodule.nodes.new("GeometryNodeSetPosition")
    set_position_004.name = "Set Position.004"
    # Position
    set_position_004.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Set Position.005
    set_position_005 = blankmodule.nodes.new("GeometryNodeSetPosition")
    set_position_005.name = "Set Position.005"
    # Position
    set_position_005.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Instance on Points
    instance_on_points = blankmodule.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.inputs[3].hide = True
    instance_on_points.inputs[4].hide = True
    instance_on_points.inputs[5].hide = True
    instance_on_points.inputs[6].hide = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    # node Group Input.006
    group_input_006 = blankmodule.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True

    # node Realize Instances
    realize_instances = blankmodule.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # node Merge by Distance
    merge_by_distance = blankmodule.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = "ALL"
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Distance
    merge_by_distance.inputs[2].default_value = 9.999999747378752e-05

    # node Mesh to Points
    mesh_to_points = blankmodule.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points.name = "Mesh to Points"
    mesh_to_points.mode = "VERTICES"
    # Selection
    mesh_to_points.inputs[1].default_value = True
    # Position
    mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    mesh_to_points.inputs[3].default_value = 0.05000000074505806

    # node Mesh to Points.001
    mesh_to_points_001 = blankmodule.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points_001.name = "Mesh to Points.001"
    mesh_to_points_001.mode = "VERTICES"
    # Selection
    mesh_to_points_001.inputs[1].default_value = True
    # Position
    mesh_to_points_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    mesh_to_points_001.inputs[3].default_value = 0.05000000074505806

    # node Instance on Points.001
    instance_on_points_001 = blankmodule.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    instance_on_points_001.inputs[1].hide = True
    instance_on_points_001.inputs[3].hide = True
    instance_on_points_001.inputs[4].hide = True
    instance_on_points_001.inputs[5].hide = True
    instance_on_points_001.inputs[6].hide = True
    # Selection
    instance_on_points_001.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0
    # Rotation
    instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)

    # node Instance on Points.002
    instance_on_points_002 = blankmodule.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_002.name = "Instance on Points.002"
    instance_on_points_002.inputs[1].hide = True
    instance_on_points_002.inputs[3].hide = True
    instance_on_points_002.inputs[4].hide = True
    instance_on_points_002.inputs[5].hide = True
    instance_on_points_002.inputs[6].hide = True
    # Selection
    instance_on_points_002.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_002.inputs[3].default_value = False
    # Instance Index
    instance_on_points_002.inputs[4].default_value = 0
    # Rotation
    instance_on_points_002.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points_002.inputs[6].default_value = (1.0, 1.0, 1.0)

    # node Transform Geometry.001
    transform_geometry_001 = blankmodule.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = "COMPONENTS"
    transform_geometry_001.inputs[2].hide = True
    transform_geometry_001.inputs[3].hide = True
    # Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Transform Geometry.002
    transform_geometry_002 = blankmodule.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = "COMPONENTS"
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    # Rotation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Group Input.007
    group_input_007 = blankmodule.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[9].hide = True
    group_input_007.outputs[10].hide = True

    # node Math.007
    math_007 = blankmodule.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = "MULTIPLY"
    math_007.use_clamp = False

    # node Math.008
    math_008 = blankmodule.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = "MULTIPLY"
    math_008.use_clamp = False
    # Value_001
    math_008.inputs[1].default_value = 2.0

    # node Math.009
    math_009 = blankmodule.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = "SUBTRACT"
    math_009.use_clamp = False

    # node Group Input.008
    group_input_008 = blankmodule.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[7].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True

    # node Math.010
    math_010 = blankmodule.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = "MULTIPLY"
    math_010.use_clamp = False

    # node Math.011
    math_011 = blankmodule.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.operation = "MULTIPLY"
    math_011.use_clamp = False
    # Value_001
    math_011.inputs[1].default_value = 2.0

    # node Math.012
    math_012 = blankmodule.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.operation = "SUBTRACT"
    math_012.use_clamp = False

    # node Combine XYZ.008
    combine_xyz_008 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_008.name = "Combine XYZ.008"
    combine_xyz_008.inputs[0].hide = True
    combine_xyz_008.inputs[2].hide = True
    # X
    combine_xyz_008.inputs[0].default_value = 0.0
    # Z
    combine_xyz_008.inputs[2].default_value = 0.0

    # node Combine XYZ.009
    combine_xyz_009 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_009.name = "Combine XYZ.009"
    combine_xyz_009.inputs[1].hide = True
    combine_xyz_009.inputs[2].hide = True
    # Y
    combine_xyz_009.inputs[1].default_value = 0.0
    # Z
    combine_xyz_009.inputs[2].default_value = 0.0

    # node Duplicate Elements
    duplicate_elements = blankmodule.nodes.new("GeometryNodeDuplicateElements")
    duplicate_elements.name = "Duplicate Elements"
    duplicate_elements.domain = "POINT"
    # Selection
    duplicate_elements.inputs[1].default_value = True
    # Amount
    duplicate_elements.inputs[2].default_value = 1

    # node Group Input.009
    group_input_009 = blankmodule.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"
    group_input_009.outputs[0].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[6].hide = True
    group_input_009.outputs[7].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True

    # node Math.013
    math_013 = blankmodule.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = "SUBTRACT"
    math_013.use_clamp = False

    # node Points
    points = blankmodule.nodes.new("GeometryNodePoints")
    points.name = "Points"
    # Count
    points.inputs[0].default_value = 1
    # Radius
    points.inputs[2].default_value = 0.05000000074505806

    # node Points.001
    points_001 = blankmodule.nodes.new("GeometryNodePoints")
    points_001.name = "Points.001"
    # Count
    points_001.inputs[0].default_value = 1
    # Radius
    points_001.inputs[2].default_value = 0.05000000074505806

    # node Math.014
    math_014 = blankmodule.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = "MULTIPLY"
    math_014.use_clamp = False
    # Value_001
    math_014.inputs[1].default_value = 2.0

    # node Combine XYZ.010
    combine_xyz_010 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_010.name = "Combine XYZ.010"
    combine_xyz_010.inputs[0].hide = True
    combine_xyz_010.inputs[2].hide = True
    # X
    combine_xyz_010.inputs[0].default_value = 0.0
    # Z
    combine_xyz_010.inputs[2].default_value = 0.0

    # node Combine XYZ.011
    combine_xyz_011 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_011.name = "Combine XYZ.011"
    combine_xyz_011.inputs[1].hide = True
    combine_xyz_011.inputs[2].hide = True
    # Y
    combine_xyz_011.inputs[1].default_value = 0.0
    # Z
    combine_xyz_011.inputs[2].default_value = 0.0

    # node Points.002
    points_002 = blankmodule.nodes.new("GeometryNodePoints")
    points_002.name = "Points.002"
    # Count
    points_002.inputs[0].default_value = 1
    # Position
    points_002.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Radius
    points_002.inputs[2].default_value = 0.05000000074505806

    # node Join Geometry
    join_geometry = blankmodule.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # node Transform Geometry.003
    transform_geometry_003 = blankmodule.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = "COMPONENTS"
    transform_geometry_003.inputs[2].hide = True
    transform_geometry_003.inputs[3].hide = True
    # Rotation
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Transform Geometry.004
    transform_geometry_004 = blankmodule.nodes.new("GeometryNodeTransform")
    transform_geometry_004.name = "Transform Geometry.004"
    transform_geometry_004.mode = "COMPONENTS"
    transform_geometry_004.inputs[2].hide = True
    transform_geometry_004.inputs[3].hide = True
    # Rotation
    transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Combine XYZ.012
    combine_xyz_012 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_012.name = "Combine XYZ.012"
    combine_xyz_012.inputs[2].hide = True
    # Z
    combine_xyz_012.inputs[2].default_value = 0.0

    # node Mesh Line
    mesh_line = blankmodule.nodes.new("GeometryNodeMeshLine")
    mesh_line.name = "Mesh Line"
    mesh_line.count_mode = "TOTAL"
    mesh_line.mode = "OFFSET"
    # Start Location
    mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Mesh Line.001
    mesh_line_001 = blankmodule.nodes.new("GeometryNodeMeshLine")
    mesh_line_001.name = "Mesh Line.001"
    mesh_line_001.count_mode = "TOTAL"
    mesh_line_001.mode = "OFFSET"
    # Start Location
    mesh_line_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Combine XYZ.013
    combine_xyz_013 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_013.name = "Combine XYZ.013"
    combine_xyz_013.inputs[1].hide = True
    combine_xyz_013.inputs[2].hide = True
    # Y
    combine_xyz_013.inputs[1].default_value = 0.0
    # Z
    combine_xyz_013.inputs[2].default_value = 0.0

    # node Combine XYZ.014
    combine_xyz_014 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_014.name = "Combine XYZ.014"
    combine_xyz_014.inputs[0].hide = True
    combine_xyz_014.inputs[2].hide = True
    # X
    combine_xyz_014.inputs[0].default_value = 0.0
    # Z
    combine_xyz_014.inputs[2].default_value = 0.0

    # node Group Input.010
    group_input_010 = blankmodule.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"
    group_input_010.outputs[0].hide = True
    group_input_010.outputs[2].hide = True
    group_input_010.outputs[6].hide = True
    group_input_010.outputs[7].hide = True
    group_input_010.outputs[8].hide = True
    group_input_010.outputs[9].hide = True
    group_input_010.outputs[10].hide = True

    # node Duplicate Elements.001
    duplicate_elements_001 = blankmodule.nodes.new("GeometryNodeDuplicateElements")
    duplicate_elements_001.name = "Duplicate Elements.001"
    duplicate_elements_001.domain = "POINT"
    # Selection
    duplicate_elements_001.inputs[1].default_value = True
    # Amount
    duplicate_elements_001.inputs[2].default_value = 1

    # node Join Geometry.001
    join_geometry_001 = blankmodule.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"

    # node Join Geometry.002
    join_geometry_002 = blankmodule.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"

    # node Math.015
    math_015 = blankmodule.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = "MULTIPLY"
    math_015.use_clamp = False

    # node Math.016
    math_016 = blankmodule.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.operation = "MULTIPLY"
    math_016.use_clamp = False

    # node Group Input.011
    group_input_011 = blankmodule.nodes.new("NodeGroupInput")
    group_input_011.name = "Group Input.011"
    group_input_011.outputs[0].hide = True
    group_input_011.outputs[2].hide = True
    group_input_011.outputs[6].hide = True
    group_input_011.outputs[7].hide = True
    group_input_011.outputs[8].hide = True
    group_input_011.outputs[9].hide = True
    group_input_011.outputs[10].hide = True

    # node Math.017
    math_017 = blankmodule.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.operation = "MULTIPLY"
    math_017.use_clamp = False
    # Value_001
    math_017.inputs[1].default_value = -0.5

    # node Math.018
    math_018 = blankmodule.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.operation = "MULTIPLY"
    math_018.use_clamp = False
    # Value_001
    math_018.inputs[1].default_value = -0.5

    # node Combine XYZ.015
    combine_xyz_015 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_015.name = "Combine XYZ.015"
    combine_xyz_015.inputs[2].hide = True
    # Z
    combine_xyz_015.inputs[2].default_value = 0.0

    # node Vector Math
    vector_math = blankmodule.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = "MULTIPLY"

    # node Group Input.012
    group_input_012 = blankmodule.nodes.new("NodeGroupInput")
    group_input_012.name = "Group Input.012"
    group_input_012.outputs[1].hide = True
    group_input_012.outputs[2].hide = True
    group_input_012.outputs[4].hide = True
    group_input_012.outputs[5].hide = True
    group_input_012.outputs[6].hide = True
    group_input_012.outputs[7].hide = True
    group_input_012.outputs[8].hide = True
    group_input_012.outputs[9].hide = True
    group_input_012.outputs[10].hide = True

    # node Math.019
    math_019 = blankmodule.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.operation = "MULTIPLY"
    math_019.use_clamp = False
    # Value_001
    math_019.inputs[1].default_value = -0.5

    # node Combine XYZ.016
    combine_xyz_016 = blankmodule.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_016.name = "Combine XYZ.016"
    combine_xyz_016.inputs[0].hide = True
    combine_xyz_016.inputs[1].hide = True
    # X
    combine_xyz_016.inputs[0].default_value = 0.0
    # Y
    combine_xyz_016.inputs[1].default_value = 0.0

    # node Group Input.013
    group_input_013 = blankmodule.nodes.new("NodeGroupInput")
    group_input_013.name = "Group Input.013"
    group_input_013.outputs[0].hide = True
    group_input_013.outputs[1].hide = True
    group_input_013.outputs[4].hide = True
    group_input_013.outputs[5].hide = True
    group_input_013.outputs[6].hide = True
    group_input_013.outputs[7].hide = True
    group_input_013.outputs[8].hide = True
    group_input_013.outputs[9].hide = True
    group_input_013.outputs[10].hide = True

    # node Vector Math.001
    vector_math_001 = blankmodule.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = "ADD"

    # node Mesh Boolean
    mesh_boolean = blankmodule.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = "DIFFERENCE"
    mesh_boolean.solver = "EXACT"
    # Self Intersection
    mesh_boolean.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean.inputs[3].default_value = False

    # node Math.020
    math_020 = blankmodule.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.operation = "MULTIPLY"
    math_020.use_clamp = False
    # Value_001
    math_020.inputs[1].default_value = 0.5

    # node Group Input.014
    group_input_014 = blankmodule.nodes.new("NodeGroupInput")
    group_input_014.name = "Group Input.014"
    group_input_014.outputs[0].hide = True
    group_input_014.outputs[1].hide = True
    group_input_014.outputs[4].hide = True
    group_input_014.outputs[5].hide = True
    group_input_014.outputs[6].hide = True
    group_input_014.outputs[8].hide = True
    group_input_014.outputs[10].hide = True

    # node Compare.006
    compare_006 = blankmodule.nodes.new("FunctionNodeCompare")
    compare_006.name = "Compare.006"
    compare_006.data_type = "FLOAT"
    compare_006.mode = "ELEMENT"
    compare_006.operation = "EQUAL"
    # B
    compare_006.inputs[1].default_value = 1.0
    # Epsilon
    compare_006.inputs[12].default_value = 0.0

    # node Separate XYZ.003
    separate_xyz_003 = blankmodule.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"
    separate_xyz_003.outputs[1].hide = True
    separate_xyz_003.outputs[2].hide = True

    # node Normal.002
    normal_002 = blankmodule.nodes.new("GeometryNodeInputNormal")
    normal_002.name = "Normal.002"

    # node Geometry to Instance
    geometry_to_instance = blankmodule.nodes.new("GeometryNodeGeometryToInstance")
    geometry_to_instance.name = "Geometry to Instance"

    # node Transform Geometry.005
    transform_geometry_005 = blankmodule.nodes.new("GeometryNodeTransform")
    transform_geometry_005.name = "Transform Geometry.005"
    transform_geometry_005.mode = "COMPONENTS"
    transform_geometry_005.inputs[2].hide = True
    transform_geometry_005.inputs[3].hide = True
    # Rotation
    transform_geometry_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_005.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Group Output
    group_output = blankmodule.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # node Store Named Attribute
    store_named_attribute = blankmodule.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = "BOOLEAN"
    store_named_attribute.domain = "EDGE"
    # Name
    store_named_attribute.inputs[2].default_value = "seam_holes"
    # Value
    store_named_attribute.inputs[3].default_value = True

    # node Cylinder
    cylinder = blankmodule.nodes.new("GeometryNodeMeshCylinder")
    cylinder.name = "Cylinder"
    cylinder.fill_type = "NONE"
    # Side Segments
    cylinder.inputs[1].default_value = 1

    # node Set Shade Smooth
    set_shade_smooth = blankmodule.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = "FACE"
    # Shade Smooth
    set_shade_smooth.inputs[2].default_value = True

    # node Join Geometry.003
    join_geometry_003 = blankmodule.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"

    # Set parents
    transform_geometry.parent = frame
    group_input.parent = frame
    cube.parent = frame
    combine_xyz.parent = frame
    combine_xyz_001.parent = frame
    group_input_001.parent = frame
    math.parent = frame
    normal.parent = frame_001
    separate_xyz.parent = frame_001
    compare.parent = frame_001
    group_input_002.parent = frame_001
    math_001.parent = frame_001
    combine_xyz_002.parent = frame_001
    math_002.parent = frame_001
    math_003.parent = frame_001
    math_004.parent = frame_001
    group_input_003.parent = frame_001
    combine_xyz_003.parent = frame_001
    compare_001.parent = frame_001
    set_position.parent = frame_001
    set_position_001.parent = frame_001
    set_position_002.parent = frame_002
    set_position_003.parent = frame_002
    combine_xyz_004.parent = frame_002
    combine_xyz_005.parent = frame_002
    math_005.parent = frame_002
    group_input_004.parent = frame_002
    compare_002.parent = frame_002
    compare_003.parent = frame_002
    separate_xyz_001.parent = frame_002
    normal_001.parent = frame_002
    separate_xyz_002.parent = frame_002
    compare_004.parent = frame_002
    compare_005.parent = frame_002
    group_input_005.parent = frame_002
    math_006.parent = frame_002
    combine_xyz_006.parent = frame_002
    combine_xyz_007.parent = frame_002
    set_position_004.parent = frame_002
    set_position_005.parent = frame_002
    instance_on_points.parent = frame_003
    group_input_006.parent = frame_003
    realize_instances.parent = frame_003
    merge_by_distance.parent = frame_003
    mesh_to_points.parent = frame_003
    mesh_to_points_001.parent = frame_003
    instance_on_points_001.parent = frame_003
    instance_on_points_002.parent = frame_003
    transform_geometry_001.parent = frame_003
    transform_geometry_002.parent = frame_003
    group_input_007.parent = frame_003
    math_007.parent = frame_003
    math_008.parent = frame_003
    math_009.parent = frame_003
    group_input_008.parent = frame_003
    math_010.parent = frame_003
    math_011.parent = frame_003
    math_012.parent = frame_003
    combine_xyz_008.parent = frame_003
    combine_xyz_009.parent = frame_003
    duplicate_elements.parent = frame_003
    group_input_009.parent = frame_003
    math_013.parent = frame_003
    points.parent = frame_003
    points_001.parent = frame_003
    math_014.parent = frame_003
    combine_xyz_010.parent = frame_003
    combine_xyz_011.parent = frame_003
    points_002.parent = frame_003
    join_geometry.parent = frame_003
    transform_geometry_003.parent = frame_003
    transform_geometry_004.parent = frame_003
    combine_xyz_012.parent = frame_003
    mesh_line.parent = frame_003
    mesh_line_001.parent = frame_003
    combine_xyz_013.parent = frame_003
    combine_xyz_014.parent = frame_003
    group_input_010.parent = frame_003
    duplicate_elements_001.parent = frame_003
    join_geometry_001.parent = frame_003
    join_geometry_002.parent = frame_003
    math_015.parent = frame_004
    math_016.parent = frame_004
    group_input_011.parent = frame_004
    math_017.parent = frame_004
    math_018.parent = frame_004
    combine_xyz_015.parent = frame_004
    vector_math.parent = frame_004
    group_input_012.parent = frame_004
    math_019.parent = frame_005
    combine_xyz_016.parent = frame_005
    group_input_013.parent = frame_005
    vector_math_001.parent = frame_005
    mesh_boolean.parent = frame_003
    math_020.parent = frame_003
    group_input_014.parent = frame_003
    compare_006.parent = frame_003
    separate_xyz_003.parent = frame_003
    normal_002.parent = frame_003
    geometry_to_instance.parent = frame_003
    store_named_attribute.parent = frame_003
    cylinder.parent = frame_003
    set_shade_smooth.parent = frame_003
    join_geometry_003.parent = frame_003

    # Set locations
    frame.location = (-8184.921875, 2045.48828125)
    frame_001.location = (-5897.60546875, 2412.5478515625)
    frame_002.location = (-5793.84423828125, 2441.30322265625)
    frame_003.location = (-444.615234375, 1014.5482788085938)
    frame_004.location = (-530.7978515625, 220.8665771484375)
    frame_005.location = (-608.75244140625, 317.6299743652344)
    transform_geometry.location = (-632.6036376953125, 45.062469482421875)
    group_input.location = (-1202.6036376953125, 32.562469482421875)
    cube.location = (-822.6036376953125, 77.06246948242188)
    combine_xyz.location = (-1012.6036376953125, 55.062469482421875)
    combine_xyz_001.location = (-818.9298095703125, -152.18344116210938)
    group_input_001.location = (-1198.9298095703125, -175.68344116210938)
    math.location = (-1008.9298095703125, -124.6834487915039)
    normal.location = (-2600.792236328125, -688.3894653320312)
    separate_xyz.location = (-2410.792236328125, -663.8894653320312)
    compare.location = (-2202.9609375, -691.4400024414062)
    group_input_002.location = (-1986.91650390625, -769.8660888671875)
    math_001.location = (-1796.91650390625, -729.8660888671875)
    combine_xyz_002.location = (-1416.91650390625, -768.3660888671875)
    math_002.location = (-1606.91650390625, -729.8660888671875)
    math_003.location = (-1602.591796875, -519.2313232421875)
    math_004.location = (-1792.591796875, -519.2313232421875)
    group_input_003.location = (-1982.591796875, -559.2313232421875)
    combine_xyz_003.location = (-1412.591796875, -557.7313232421875)
    compare_001.location = (-2202.9609375, -522.4400024414062)
    set_position.location = (-1199.119384765625, -285.128173828125)
    set_position_001.location = (-950.6165161132812, -579.2698974609375)
    set_position_002.location = (1901.6348876953125, -1149.798095703125)
    set_position_003.location = (1685.6138916015625, -881.1987915039062)
    combine_xyz_004.location = (1484.8563232421875, -1016.313232421875)
    combine_xyz_005.location = (1484.8563232421875, -1143.90771484375)
    math_005.location = (1288.50830078125, -1038.09423828125)
    group_input_004.location = (1093.5130615234375, -1161.686279296875)
    compare_002.location = (907.4673461914062, -1027.34765625)
    compare_003.location = (907.4673461914062, -1196.34765625)
    separate_xyz_001.location = (715.796142578125, -1170.029541015625)
    normal_001.location = (-706.6566162109375, -1023.052978515625)
    separate_xyz_002.location = (-472.5413513183594, -866.019775390625)
    compare_004.location = (-280.8701477050781, -892.3379516601562)
    compare_005.location = (-280.8701477050781, -723.337890625)
    group_input_005.location = (-94.82441711425781, -857.676513671875)
    math_006.location = (100.17082214355469, -734.08447265625)
    combine_xyz_006.location = (296.5188293457031, -839.89794921875)
    combine_xyz_007.location = (296.5188293457031, -712.303466796875)
    set_position_004.location = (497.2763977050781, -577.1890869140625)
    set_position_005.location = (713.2974243164062, -845.788330078125)
    instance_on_points.location = (-3476.369140625, -1264.945556640625)
    group_input_006.location = (-3797.7763671875, -1308.520751953125)
    realize_instances.location = (-4827.376953125, -879.7869873046875)
    merge_by_distance.location = (-4637.376953125, -842.7869873046875)
    mesh_to_points.location = (-6536.9853515625, -649.318603515625)
    mesh_to_points_001.location = (-6535.70166015625, -1161.8203125)
    instance_on_points_001.location = (-6352.9990234375, -483.599365234375)
    instance_on_points_002.location = (-6352.9990234375, -1325.7928466796875)
    transform_geometry_001.location = (-5339.39794921875, -402.599365234375)
    transform_geometry_002.location = (-5339.39794921875, -1244.7928466796875)
    group_input_007.location = (-6144.2470703125, -629.9935302734375)
    math_007.location = (-5954.2470703125, -550.1070556640625)
    math_008.location = (-5951.7841796875, -720.726318359375)
    math_009.location = (-5728.86572265625, -627.933349609375)
    group_input_008.location = (-6142.41357421875, -1407.496826171875)
    math_010.location = (-5952.41357421875, -1327.6103515625)
    math_011.location = (-5949.951171875, -1498.2296142578125)
    math_012.location = (-5727.0322265625, -1405.4366455078125)
    combine_xyz_008.location = (-5532.04443359375, -1406.0213623046875)
    combine_xyz_009.location = (-5533.8779296875, -628.5179443359375)
    duplicate_elements.location = (-5602.50048828125, -1182.634521484375)
    group_input_009.location = (-8944.658203125, -1104.2965087890625)
    math_013.location = (-8488.068359375, -1026.1923828125)
    points.location = (-7983.822265625, -1082.4669189453125)
    points_001.location = (-7983.822265625, -948.4669189453125)
    math_014.location = (-8724.419921875, -1199.1781005859375)
    combine_xyz_010.location = (-8221.30078125, -995.046142578125)
    combine_xyz_011.location = (-8221.30078125, -1127.0455322265625)
    points_002.location = (-7983.822265625, -720.71728515625)
    join_geometry.location = (-7760.1640625, -1061.3992919921875)
    transform_geometry_003.location = (-7495.4501953125, -900.9609375)
    transform_geometry_004.location = (-7495.4501953125, -1035.23095703125)
    combine_xyz_012.location = (-7760.4423828125, -1207.90234375)
    mesh_line.location = (-6726.9853515625, -780.756591796875)
    mesh_line_001.location = (-6725.7021484375, -1024.68505859375)
    combine_xyz_013.location = (-6915.7021484375, -1110.3203125)
    combine_xyz_014.location = (-6916.65283203125, -920.182373046875)
    group_input_010.location = (-7114.283203125, -981.017822265625)
    duplicate_elements_001.location = (-5602.50048828125, -340.4410400390625)
    join_geometry_001.location = (-5017.376953125, -874.7869873046875)
    join_geometry_002.location = (-6112.875, -908.308837890625)
    math_015.location = (-1634.18310546875, -509.2121276855469)
    math_016.location = (-1634.18310546875, -340.2121276855469)
    group_input_011.location = (-1836.93603515625, -470.1422119140625)
    math_017.location = (-1456.55908203125, -508.96429443359375)
    math_018.location = (-1456.55908203125, -339.96429443359375)
    combine_xyz_015.location = (-1208.8779296875, -456.9739074707031)
    vector_math.location = (-1012.79833984375, -386.2425842285156)
    group_input_012.location = (-1212.09765625, -387.7550354003906)
    math_019.location = (-926.01953125, -149.020263671875)
    combine_xyz_016.location = (-751.80712890625, -131.4840087890625)
    group_input_013.location = (-1102.30224609375, -227.88442993164062)
    vector_math_001.location = (-505.8935546875, -193.17498779296875)
    mesh_boolean.location = (-2533.68994140625, -626.8739013671875)
    math_020.location = (-5413.71044921875, -1934.98095703125)
    group_input_014.location = (-5593.56103515625, -1769.2479248046875)
    compare_006.location = (-4549.70556640625, -1834.489013671875)
    separate_xyz_003.location = (-4739.70556640625, -1882.989013671875)
    normal_002.location = (-4929.70556640625, -1896.489013671875)
    geometry_to_instance.location = (-3925.556884765625, -1573.0072021484375)
    transform_geometry_005.location = (-724.41845703125, 409.9898376464844)
    group_output.location = (1108.9892578125, 403.5124206542969)
    store_named_attribute.location = (-4323.96484375, -1700.503173828125)
    cylinder.location = (-5150.81787109375, -1749.5826416015625)
    set_shade_smooth.location = (-4737.7041015625, -1735.38330078125)
    join_geometry_003.location = (-7760.1640625, -925.5980224609375)

    # Set dimensions
    frame.width, frame.height = 770.0, 420.0
    frame_001.width, frame_001.height = 1850.0, 662.0
    frame_002.width, frame_002.height = 2809.0, 837.0
    frame_003.width, frame_003.height = 6611.0, 1812.0
    frame_004.width, frame_004.height = 1024.0, 387.0
    frame_005.width, frame_005.height = 796.0, 257.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    cube.width, cube.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    set_position_003.width, set_position_003.height = 140.0, 100.0
    combine_xyz_004.width, combine_xyz_004.height = 140.0, 100.0
    combine_xyz_005.width, combine_xyz_005.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    normal_001.width, normal_001.height = 140.0, 100.0
    separate_xyz_002.width, separate_xyz_002.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0
    compare_005.width, compare_005.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    combine_xyz_006.width, combine_xyz_006.height = 140.0, 100.0
    combine_xyz_007.width, combine_xyz_007.height = 140.0, 100.0
    set_position_004.width, set_position_004.height = 140.0, 100.0
    set_position_005.width, set_position_005.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
    mesh_to_points_001.width, mesh_to_points_001.height = 140.0, 100.0
    instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
    instance_on_points_002.width, instance_on_points_002.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    math_009.width, math_009.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    math_010.width, math_010.height = 140.0, 100.0
    math_011.width, math_011.height = 140.0, 100.0
    math_012.width, math_012.height = 140.0, 100.0
    combine_xyz_008.width, combine_xyz_008.height = 140.0, 100.0
    combine_xyz_009.width, combine_xyz_009.height = 140.0, 100.0
    duplicate_elements.width, duplicate_elements.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    math_013.width, math_013.height = 140.0, 100.0
    points.width, points.height = 140.0, 100.0
    points_001.width, points_001.height = 140.0, 100.0
    math_014.width, math_014.height = 140.0, 100.0
    combine_xyz_010.width, combine_xyz_010.height = 140.0, 100.0
    combine_xyz_011.width, combine_xyz_011.height = 140.0, 100.0
    points_002.width, points_002.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
    combine_xyz_012.width, combine_xyz_012.height = 140.0, 100.0
    mesh_line.width, mesh_line.height = 140.0, 100.0
    mesh_line_001.width, mesh_line_001.height = 140.0, 100.0
    combine_xyz_013.width, combine_xyz_013.height = 140.0, 100.0
    combine_xyz_014.width, combine_xyz_014.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    duplicate_elements_001.width, duplicate_elements_001.height = 140.0, 100.0
    join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
    join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
    math_015.width, math_015.height = 140.0, 100.0
    math_016.width, math_016.height = 140.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    math_017.width, math_017.height = 140.0, 100.0
    math_018.width, math_018.height = 140.0, 100.0
    combine_xyz_015.width, combine_xyz_015.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    math_019.width, math_019.height = 140.0, 100.0
    combine_xyz_016.width, combine_xyz_016.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    math_020.width, math_020.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    compare_006.width, compare_006.height = 140.0, 100.0
    separate_xyz_003.width, separate_xyz_003.height = 140.0, 100.0
    normal_002.width, normal_002.height = 140.0, 100.0
    geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
    transform_geometry_005.width, transform_geometry_005.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    store_named_attribute.width, store_named_attribute.height = 166.968994140625, 100.0
    cylinder.width, cylinder.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    join_geometry_003.width, join_geometry_003.height = 140.0, 100.0

    # initialize blankmodule links
    # combine_xyz.Vector -> cube.Size
    blankmodule.links.new(combine_xyz.outputs[0], cube.inputs[0])
    # group_input.module_size -> combine_xyz.X
    blankmodule.links.new(group_input.outputs[1], combine_xyz.inputs[0])
    # group_input.module_size -> combine_xyz.Y
    blankmodule.links.new(group_input.outputs[1], combine_xyz.inputs[1])
    # group_input.module_thickness -> combine_xyz.Z
    blankmodule.links.new(group_input.outputs[2], combine_xyz.inputs[2])
    # cube.Mesh -> transform_geometry.Geometry
    blankmodule.links.new(cube.outputs[0], transform_geometry.inputs[0])
    # combine_xyz_001.Vector -> transform_geometry.Translation
    blankmodule.links.new(combine_xyz_001.outputs[0], transform_geometry.inputs[1])
    # normal.Normal -> compare_001.A
    blankmodule.links.new(normal.outputs[0], compare_001.inputs[4])
    # normal.Normal -> separate_xyz.Vector
    blankmodule.links.new(normal.outputs[0], separate_xyz.inputs[0])
    # separate_xyz.X -> compare_001.A
    blankmodule.links.new(separate_xyz.outputs[0], compare_001.inputs[0])
    # math_004.Value -> math_003.Value
    blankmodule.links.new(math_004.outputs[0], math_003.inputs[1])
    # group_input_003.module_size -> math_003.Value
    blankmodule.links.new(group_input_003.outputs[1], math_003.inputs[0])
    # group_input_003.module_count_x -> math_004.Value
    blankmodule.links.new(group_input_003.outputs[4], math_004.inputs[0])
    # math_001.Value -> math_002.Value
    blankmodule.links.new(math_001.outputs[0], math_002.inputs[1])
    # group_input_002.module_size -> math_002.Value
    blankmodule.links.new(group_input_002.outputs[1], math_002.inputs[0])
    # group_input_002.module_count_y -> math_001.Value
    blankmodule.links.new(group_input_002.outputs[5], math_001.inputs[0])
    # separate_xyz.Y -> compare.A
    blankmodule.links.new(separate_xyz.outputs[1], compare.inputs[0])
    # transform_geometry.Geometry -> set_position.Geometry
    blankmodule.links.new(transform_geometry.outputs[0], set_position.inputs[0])
    # math_003.Value -> combine_xyz_003.X
    blankmodule.links.new(math_003.outputs[0], combine_xyz_003.inputs[0])
    # combine_xyz_003.Vector -> set_position.Offset
    blankmodule.links.new(combine_xyz_003.outputs[0], set_position.inputs[3])
    # compare_001.Result -> set_position.Selection
    blankmodule.links.new(compare_001.outputs[0], set_position.inputs[1])
    # math_002.Value -> combine_xyz_002.Y
    blankmodule.links.new(math_002.outputs[0], combine_xyz_002.inputs[1])
    # combine_xyz_002.Vector -> set_position_001.Offset
    blankmodule.links.new(combine_xyz_002.outputs[0], set_position_001.inputs[3])
    # set_position.Geometry -> set_position_001.Geometry
    blankmodule.links.new(set_position.outputs[0], set_position_001.inputs[0])
    # compare.Result -> set_position_001.Selection
    blankmodule.links.new(compare.outputs[0], set_position_001.inputs[1])
    # geometry_to_instance.Instances -> instance_on_points.Instance
    blankmodule.links.new(geometry_to_instance.outputs[0], instance_on_points.inputs[2])
    # instance_on_points.Instances -> mesh_boolean.Mesh 2
    blankmodule.links.new(instance_on_points.outputs[0], mesh_boolean.inputs[1])
    # group_input_014.holes_vertices -> cylinder.Vertices
    blankmodule.links.new(group_input_014.outputs[7], cylinder.inputs[0])
    # math_014.Value -> math_013.Value
    blankmodule.links.new(math_014.outputs[0], math_013.inputs[1])
    # group_input_009.module_size -> math_013.Value
    blankmodule.links.new(group_input_009.outputs[1], math_013.inputs[0])
    # group_input_009.holes_offset_from_corner -> math_014.Value
    blankmodule.links.new(group_input_009.outputs[8], math_014.inputs[0])
    # math_013.Value -> combine_xyz_011.X
    blankmodule.links.new(math_013.outputs[0], combine_xyz_011.inputs[0])
    # combine_xyz_011.Vector -> points.Position
    blankmodule.links.new(combine_xyz_011.outputs[0], points.inputs[1])
    # points_002.Points -> join_geometry.Geometry
    blankmodule.links.new(points_002.outputs[0], join_geometry.inputs[0])
    # join_geometry.Geometry -> transform_geometry_004.Geometry
    blankmodule.links.new(join_geometry.outputs[0], transform_geometry_004.inputs[0])
    # group_input_006.holes_enable -> instance_on_points.Selection
    blankmodule.links.new(group_input_006.outputs[6], instance_on_points.inputs[1])
    # combine_xyz_012.Vector -> transform_geometry_004.Translation
    blankmodule.links.new(combine_xyz_012.outputs[0], transform_geometry_004.inputs[1])
    # mesh_line_001.Mesh -> mesh_to_points_001.Mesh
    blankmodule.links.new(mesh_line_001.outputs[0], mesh_to_points_001.inputs[0])
    # mesh_to_points_001.Points -> instance_on_points_002.Points
    blankmodule.links.new(
        mesh_to_points_001.outputs[0], instance_on_points_002.inputs[0]
    )
    # transform_geometry_004.Geometry -> instance_on_points_002.Instance
    blankmodule.links.new(
        transform_geometry_004.outputs[0], instance_on_points_002.inputs[2]
    )
    # group_input_010.module_count_x -> mesh_line_001.Count
    blankmodule.links.new(group_input_010.outputs[4], mesh_line_001.inputs[0])
    # group_input_010.module_size -> combine_xyz_013.X
    blankmodule.links.new(group_input_010.outputs[1], combine_xyz_013.inputs[0])
    # combine_xyz_013.Vector -> mesh_line_001.Offset
    blankmodule.links.new(combine_xyz_013.outputs[0], mesh_line_001.inputs[3])
    # points_002.Points -> join_geometry_003.Geometry
    blankmodule.links.new(points_002.outputs[0], join_geometry_003.inputs[0])
    # math_013.Value -> combine_xyz_010.Y
    blankmodule.links.new(math_013.outputs[0], combine_xyz_010.inputs[1])
    # combine_xyz_010.Vector -> points_001.Position
    blankmodule.links.new(combine_xyz_010.outputs[0], points_001.inputs[1])
    # combine_xyz_012.Vector -> transform_geometry_003.Translation
    blankmodule.links.new(combine_xyz_012.outputs[0], transform_geometry_003.inputs[1])
    # join_geometry_003.Geometry -> transform_geometry_003.Geometry
    blankmodule.links.new(
        join_geometry_003.outputs[0], transform_geometry_003.inputs[0]
    )
    # transform_geometry_003.Geometry -> instance_on_points_001.Points
    blankmodule.links.new(
        transform_geometry_003.outputs[0], instance_on_points_001.inputs[0]
    )
    # mesh_line.Mesh -> mesh_to_points.Mesh
    blankmodule.links.new(mesh_line.outputs[0], mesh_to_points.inputs[0])
    # combine_xyz_014.Vector -> mesh_line.Offset
    blankmodule.links.new(combine_xyz_014.outputs[0], mesh_line.inputs[3])
    # mesh_to_points.Points -> instance_on_points_001.Instance
    blankmodule.links.new(mesh_to_points.outputs[0], instance_on_points_001.inputs[2])
    # merge_by_distance.Geometry -> instance_on_points.Points
    blankmodule.links.new(merge_by_distance.outputs[0], instance_on_points.inputs[0])
    # instance_on_points_001.Instances -> duplicate_elements_001.Geometry
    blankmodule.links.new(
        instance_on_points_001.outputs[0], duplicate_elements_001.inputs[0]
    )
    # duplicate_elements_001.Geometry -> transform_geometry_001.Geometry
    blankmodule.links.new(
        duplicate_elements_001.outputs[0], transform_geometry_001.inputs[0]
    )
    # combine_xyz_009.Vector -> transform_geometry_001.Translation
    blankmodule.links.new(combine_xyz_009.outputs[0], transform_geometry_001.inputs[1])
    # group_input_007.module_size -> math_007.Value
    blankmodule.links.new(group_input_007.outputs[1], math_007.inputs[0])
    # math_009.Value -> combine_xyz_009.X
    blankmodule.links.new(math_009.outputs[0], combine_xyz_009.inputs[0])
    # math_007.Value -> math_009.Value
    blankmodule.links.new(math_007.outputs[0], math_009.inputs[0])
    # group_input_007.holes_offset_from_corner -> math_008.Value
    blankmodule.links.new(group_input_007.outputs[8], math_008.inputs[0])
    # math_008.Value -> math_009.Value
    blankmodule.links.new(math_008.outputs[0], math_009.inputs[1])
    # group_input_007.module_count_x -> math_007.Value
    blankmodule.links.new(group_input_007.outputs[4], math_007.inputs[1])
    # duplicate_elements.Geometry -> transform_geometry_002.Geometry
    blankmodule.links.new(
        duplicate_elements.outputs[0], transform_geometry_002.inputs[0]
    )
    # combine_xyz_008.Vector -> transform_geometry_002.Translation
    blankmodule.links.new(combine_xyz_008.outputs[0], transform_geometry_002.inputs[1])
    # group_input_008.module_size -> math_010.Value
    blankmodule.links.new(group_input_008.outputs[1], math_010.inputs[0])
    # math_010.Value -> math_012.Value
    blankmodule.links.new(math_010.outputs[0], math_012.inputs[0])
    # group_input_008.holes_offset_from_corner -> math_011.Value
    blankmodule.links.new(group_input_008.outputs[8], math_011.inputs[0])
    # math_011.Value -> math_012.Value
    blankmodule.links.new(math_011.outputs[0], math_012.inputs[1])
    # instance_on_points_002.Instances -> duplicate_elements.Geometry
    blankmodule.links.new(
        instance_on_points_002.outputs[0], duplicate_elements.inputs[0]
    )
    # group_input_008.module_count_y -> math_010.Value
    blankmodule.links.new(group_input_008.outputs[5], math_010.inputs[1])
    # math_012.Value -> combine_xyz_008.Y
    blankmodule.links.new(math_012.outputs[0], combine_xyz_008.inputs[1])
    # realize_instances.Geometry -> merge_by_distance.Geometry
    blankmodule.links.new(realize_instances.outputs[0], merge_by_distance.inputs[0])
    # join_geometry_001.Geometry -> realize_instances.Geometry
    blankmodule.links.new(join_geometry_001.outputs[0], realize_instances.inputs[0])
    # group_input_014.holes_diameter -> math_020.Value
    blankmodule.links.new(group_input_014.outputs[9], math_020.inputs[0])
    # math_020.Value -> cylinder.Radius
    blankmodule.links.new(math_020.outputs[0], cylinder.inputs[3])
    # math.Value -> combine_xyz_001.X
    blankmodule.links.new(math.outputs[0], combine_xyz_001.inputs[0])
    # math.Value -> combine_xyz_001.Y
    blankmodule.links.new(math.outputs[0], combine_xyz_001.inputs[1])
    # group_input_009.holes_offset_from_corner -> combine_xyz_012.X
    blankmodule.links.new(group_input_009.outputs[8], combine_xyz_012.inputs[0])
    # group_input_009.holes_offset_from_corner -> combine_xyz_012.Y
    blankmodule.links.new(group_input_009.outputs[8], combine_xyz_012.inputs[1])
    # mesh_boolean.Mesh -> transform_geometry_005.Geometry
    blankmodule.links.new(mesh_boolean.outputs[0], transform_geometry_005.inputs[0])
    # group_input_011.module_count_x -> math_016.Value
    blankmodule.links.new(group_input_011.outputs[4], math_016.inputs[1])
    # group_input_011.module_size -> math_016.Value
    blankmodule.links.new(group_input_011.outputs[1], math_016.inputs[0])
    # math_016.Value -> math_018.Value
    blankmodule.links.new(math_016.outputs[0], math_018.inputs[0])
    # math_018.Value -> combine_xyz_015.X
    blankmodule.links.new(math_018.outputs[0], combine_xyz_015.inputs[0])
    # math_015.Value -> math_017.Value
    blankmodule.links.new(math_015.outputs[0], math_017.inputs[0])
    # group_input_011.module_count_y -> math_015.Value
    blankmodule.links.new(group_input_011.outputs[5], math_015.inputs[1])
    # group_input_011.module_size -> math_015.Value
    blankmodule.links.new(group_input_011.outputs[1], math_015.inputs[0])
    # math_017.Value -> combine_xyz_015.Y
    blankmodule.links.new(math_017.outputs[0], combine_xyz_015.inputs[1])
    # compare_002.Result -> set_position_003.Selection
    blankmodule.links.new(compare_002.outputs[0], set_position_003.inputs[1])
    # group_input_004.module_size_tolerance -> math_005.Value
    blankmodule.links.new(group_input_004.outputs[3], math_005.inputs[0])
    # combine_xyz_004.Vector -> set_position_003.Offset
    blankmodule.links.new(combine_xyz_004.outputs[0], set_position_003.inputs[3])
    # compare_003.Result -> set_position_002.Selection
    blankmodule.links.new(compare_003.outputs[0], set_position_002.inputs[1])
    # combine_xyz_005.Vector -> set_position_002.Offset
    blankmodule.links.new(combine_xyz_005.outputs[0], set_position_002.inputs[3])
    # set_position_003.Geometry -> set_position_002.Geometry
    blankmodule.links.new(set_position_003.outputs[0], set_position_002.inputs[0])
    # separate_xyz_001.Y -> compare_003.A
    blankmodule.links.new(separate_xyz_001.outputs[1], compare_003.inputs[0])
    # separate_xyz_001.Y -> compare_002.A
    blankmodule.links.new(separate_xyz_001.outputs[1], compare_002.inputs[0])
    # group_input_004.module_size_tolerance -> combine_xyz_005.Y
    blankmodule.links.new(group_input_004.outputs[3], combine_xyz_005.inputs[1])
    # math_005.Value -> combine_xyz_004.Y
    blankmodule.links.new(math_005.outputs[0], combine_xyz_004.inputs[1])
    # set_position_002.Geometry -> mesh_boolean.Mesh 1
    blankmodule.links.new(set_position_002.outputs[0], mesh_boolean.inputs[0])
    # group_input_014.module_thickness -> cylinder.Depth
    blankmodule.links.new(group_input_014.outputs[2], cylinder.inputs[4])
    # normal_001.Normal -> separate_xyz_001.Vector
    blankmodule.links.new(normal_001.outputs[0], separate_xyz_001.inputs[0])
    # math_019.Value -> combine_xyz_016.Z
    blankmodule.links.new(math_019.outputs[0], combine_xyz_016.inputs[2])
    # vector_math_001.Vector -> transform_geometry_005.Translation
    blankmodule.links.new(vector_math_001.outputs[0], transform_geometry_005.inputs[1])
    # group_input_001.module_size -> math.Value
    blankmodule.links.new(group_input_001.outputs[1], math.inputs[0])
    # compare_005.Result -> set_position_004.Selection
    blankmodule.links.new(compare_005.outputs[0], set_position_004.inputs[1])
    # group_input_005.module_size_tolerance -> math_006.Value
    blankmodule.links.new(group_input_005.outputs[3], math_006.inputs[0])
    # combine_xyz_007.Vector -> set_position_004.Offset
    blankmodule.links.new(combine_xyz_007.outputs[0], set_position_004.inputs[3])
    # compare_004.Result -> set_position_005.Selection
    blankmodule.links.new(compare_004.outputs[0], set_position_005.inputs[1])
    # combine_xyz_006.Vector -> set_position_005.Offset
    blankmodule.links.new(combine_xyz_006.outputs[0], set_position_005.inputs[3])
    # set_position_004.Geometry -> set_position_005.Geometry
    blankmodule.links.new(set_position_004.outputs[0], set_position_005.inputs[0])
    # set_position_005.Geometry -> set_position_003.Geometry
    blankmodule.links.new(set_position_005.outputs[0], set_position_003.inputs[0])
    # set_position_001.Geometry -> set_position_004.Geometry
    blankmodule.links.new(set_position_001.outputs[0], set_position_004.inputs[0])
    # math_006.Value -> combine_xyz_007.X
    blankmodule.links.new(math_006.outputs[0], combine_xyz_007.inputs[0])
    # group_input_005.module_size_tolerance -> combine_xyz_006.X
    blankmodule.links.new(group_input_005.outputs[3], combine_xyz_006.inputs[0])
    # separate_xyz_002.X -> compare_005.A
    blankmodule.links.new(separate_xyz_002.outputs[0], compare_005.inputs[0])
    # separate_xyz_002.X -> compare_004.A
    blankmodule.links.new(separate_xyz_002.outputs[0], compare_004.inputs[0])
    # normal_001.Normal -> separate_xyz_002.Vector
    blankmodule.links.new(normal_001.outputs[0], separate_xyz_002.inputs[0])
    # group_input_010.module_size -> combine_xyz_014.Y
    blankmodule.links.new(group_input_010.outputs[1], combine_xyz_014.inputs[1])
    # group_input_010.module_count_y -> mesh_line.Count
    blankmodule.links.new(group_input_010.outputs[5], mesh_line.inputs[0])
    # instance_on_points_001.Instances -> join_geometry_002.Geometry
    blankmodule.links.new(
        instance_on_points_001.outputs[0], join_geometry_002.inputs[0]
    )
    # transform_geometry_002.Geometry -> join_geometry_001.Geometry
    blankmodule.links.new(
        transform_geometry_002.outputs[0], join_geometry_001.inputs[0]
    )
    # group_input_013.module_thickness -> math_019.Value
    blankmodule.links.new(group_input_013.outputs[2], math_019.inputs[0])
    # combine_xyz_015.Vector -> vector_math.Vector
    blankmodule.links.new(combine_xyz_015.outputs[0], vector_math.inputs[1])
    # vector_math.Vector -> vector_math_001.Vector
    blankmodule.links.new(vector_math.outputs[0], vector_math_001.inputs[1])
    # combine_xyz_016.Vector -> vector_math_001.Vector
    blankmodule.links.new(combine_xyz_016.outputs[0], vector_math_001.inputs[0])
    # group_input_012.module_centering -> vector_math.Vector
    blankmodule.links.new(group_input_012.outputs[0], vector_math.inputs[0])
    # store_named_attribute.Geometry -> geometry_to_instance.Geometry
    blankmodule.links.new(
        store_named_attribute.outputs[0], geometry_to_instance.inputs[0]
    )
    # set_shade_smooth.Geometry -> store_named_attribute.Geometry
    blankmodule.links.new(set_shade_smooth.outputs[0], store_named_attribute.inputs[0])
    # compare_006.Result -> store_named_attribute.Selection
    blankmodule.links.new(compare_006.outputs[0], store_named_attribute.inputs[1])
    # separate_xyz_003.X -> compare_006.A
    blankmodule.links.new(separate_xyz_003.outputs[0], compare_006.inputs[0])
    # normal_002.Normal -> separate_xyz_003.Vector
    blankmodule.links.new(normal_002.outputs[0], separate_xyz_003.inputs[0])
    # transform_geometry_005.Geometry -> group_output.Geometry
    blankmodule.links.new(transform_geometry_005.outputs[0], group_output.inputs[0])
    # cylinder.Mesh -> set_shade_smooth.Geometry
    blankmodule.links.new(cylinder.outputs[0], set_shade_smooth.inputs[0])
    # cylinder.Side -> set_shade_smooth.Selection
    blankmodule.links.new(cylinder.outputs[2], set_shade_smooth.inputs[1])
    # points_001.Points -> join_geometry_003.Geometry
    blankmodule.links.new(points_001.outputs[0], join_geometry_003.inputs[0])
    # points.Points -> join_geometry.Geometry
    blankmodule.links.new(points.outputs[0], join_geometry.inputs[0])
    # instance_on_points_002.Instances -> join_geometry_002.Geometry
    blankmodule.links.new(
        instance_on_points_002.outputs[0], join_geometry_002.inputs[0]
    )
    # join_geometry_002.Geometry -> join_geometry_001.Geometry
    blankmodule.links.new(join_geometry_002.outputs[0], join_geometry_001.inputs[0])
    # transform_geometry_001.Geometry -> join_geometry_001.Geometry
    blankmodule.links.new(
        transform_geometry_001.outputs[0], join_geometry_001.inputs[0]
    )
    return blankmodule


blankmodule = blankmodule_node_group()
