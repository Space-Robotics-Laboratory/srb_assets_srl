import bpy
import mathutils


# initialize _get_parallel_vectors node group
def _get_parallel_vectors_node_group():
    _get_parallel_vectors = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="_get_parallel_vectors"
    )

    _get_parallel_vectors.color_tag = "NONE"
    _get_parallel_vectors.description = ""
    _get_parallel_vectors.default_group_node_width = 140

    # _get_parallel_vectors interface
    # Socket output_x
    output_x_socket = _get_parallel_vectors.interface.new_socket(
        name="output_x", in_out="OUTPUT", socket_type="NodeSocketVector"
    )
    output_x_socket.default_value = (0.0, 0.0, 0.0)
    output_x_socket.min_value = -3.4028234663852886e38
    output_x_socket.max_value = 3.4028234663852886e38
    output_x_socket.subtype = "XYZ"
    output_x_socket.attribute_domain = "POINT"

    # Socket output_y
    output_y_socket = _get_parallel_vectors.interface.new_socket(
        name="output_y", in_out="OUTPUT", socket_type="NodeSocketVector"
    )
    output_y_socket.default_value = (0.0, 0.0, 0.0)
    output_y_socket.min_value = -3.4028234663852886e38
    output_y_socket.max_value = 3.4028234663852886e38
    output_y_socket.subtype = "XYZ"
    output_y_socket.attribute_domain = "POINT"

    # Socket input_z
    input_z_socket = _get_parallel_vectors.interface.new_socket(
        name="input_z", in_out="INPUT", socket_type="NodeSocketVector"
    )
    input_z_socket.default_value = (0.0, 0.0, 0.0)
    input_z_socket.min_value = -10000.0
    input_z_socket.max_value = 10000.0
    input_z_socket.subtype = "XYZ"
    input_z_socket.attribute_domain = "POINT"

    # initialize _get_parallel_vectors nodes
    # node Group Input
    group_input = _get_parallel_vectors.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[1].hide = True

    # node Math
    math = _get_parallel_vectors.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = "DIVIDE"
    math.use_clamp = False

    # node Combine XYZ
    combine_xyz = _get_parallel_vectors.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    # X
    combine_xyz.inputs[0].default_value = 1.0
    # Y
    combine_xyz.inputs[1].default_value = 0.0

    # node Separate XYZ
    separate_xyz = _get_parallel_vectors.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.outputs[1].hide = True

    # node Vector Math
    vector_math = _get_parallel_vectors.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = "NORMALIZE"

    # node Vector Math.001
    vector_math_001 = _get_parallel_vectors.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = "CROSS_PRODUCT"

    # node Math.001
    math_001 = _get_parallel_vectors.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = "MULTIPLY"
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = -1.0

    # node Group Output
    group_output = _get_parallel_vectors.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_output.inputs[2].hide = True

    # Set locations
    group_input.location = (-526.127197265625, -91.06910705566406)
    math.location = (43.872802734375, 50.398521423339844)
    combine_xyz.location = (233.872802734375, 32.898521423339844)
    separate_xyz.location = (-336.127197265625, 21.898521423339844)
    vector_math.location = (423.872802734375, 27.898521423339844)
    vector_math_001.location = (613.872802734375, -51.56910705566406)
    math_001.location = (-146.127197265625, 133.32717895507812)
    group_output.location = (803.872802734375, 10.398521423339844)

    # Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0

    # initialize _get_parallel_vectors links
    # math_001.Value -> math.Value
    _get_parallel_vectors.links.new(math_001.outputs[0], math.inputs[0])
    # math.Value -> combine_xyz.Z
    _get_parallel_vectors.links.new(math.outputs[0], combine_xyz.inputs[2])
    # separate_xyz.X -> math_001.Value
    _get_parallel_vectors.links.new(separate_xyz.outputs[0], math_001.inputs[0])
    # separate_xyz.Z -> math.Value
    _get_parallel_vectors.links.new(separate_xyz.outputs[2], math.inputs[1])
    # vector_math.Vector -> group_output.output_x
    _get_parallel_vectors.links.new(vector_math.outputs[0], group_output.inputs[0])
    # vector_math_001.Vector -> group_output.output_y
    _get_parallel_vectors.links.new(vector_math_001.outputs[0], group_output.inputs[1])
    # group_input.input_z -> separate_xyz.Vector
    _get_parallel_vectors.links.new(group_input.outputs[0], separate_xyz.inputs[0])
    # group_input.input_z -> vector_math_001.Vector
    _get_parallel_vectors.links.new(group_input.outputs[0], vector_math_001.inputs[1])
    # combine_xyz.Vector -> vector_math.Vector
    _get_parallel_vectors.links.new(combine_xyz.outputs[0], vector_math.inputs[0])
    # vector_math.Vector -> vector_math_001.Vector
    _get_parallel_vectors.links.new(vector_math.outputs[0], vector_math_001.inputs[0])
    return _get_parallel_vectors


_get_parallel_vectors = _get_parallel_vectors_node_group()


# initialize _decimate_planar node group
def _decimate_planar_node_group():
    _decimate_planar = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="_decimate_planar"
    )

    _decimate_planar.color_tag = "NONE"
    _decimate_planar.description = ""
    _decimate_planar.default_group_node_width = 140

    _decimate_planar.is_modifier = True

    # _decimate_planar interface
    # Socket Geometry
    geometry_socket = _decimate_planar.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket.attribute_domain = "POINT"

    # Socket Geometry
    geometry_socket_1 = _decimate_planar.interface.new_socket(
        name="Geometry", in_out="INPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket_1.attribute_domain = "POINT"

    # initialize _decimate_planar nodes
    # node Frame
    frame = _decimate_planar.nodes.new("NodeFrame")
    frame.label = "Transfer Normals"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # node Frame.001
    frame_001 = _decimate_planar.nodes.new("NodeFrame")
    frame_001.label = "Create new Faces"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # node Frame.002
    frame_002 = _decimate_planar.nodes.new("NodeFrame")
    frame_002.label = "Resample Curves"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # node Frame.003
    frame_003 = _decimate_planar.nodes.new("NodeFrame")
    frame_003.label = "Instantiate new curves"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # node Frame.004
    frame_004 = _decimate_planar.nodes.new("NodeFrame")
    frame_004.label = "Transfer original Positions"
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    # node Frame.005
    frame_005 = _decimate_planar.nodes.new("NodeFrame")
    frame_005.label = "Remove Edges"
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    # node Frame.006
    frame_006 = _decimate_planar.nodes.new("NodeFrame")
    frame_006.label = "Compare Directions to previous and next Point"
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    # node Frame.007
    frame_007 = _decimate_planar.nodes.new("NodeFrame")
    frame_007.label = "Wrap Index  within a Spline"
    frame_007.name = "Frame.007"
    frame_007.label_size = 20
    frame_007.shrink = True

    # node Frame.008
    frame_008 = _decimate_planar.nodes.new("NodeFrame")
    frame_008.label = "Split Geometry at sharp Edges"
    frame_008.name = "Frame.008"
    frame_008.label_size = 20
    frame_008.shrink = True

    # node Join Geometry
    join_geometry = _decimate_planar.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # node Merge by Distance
    merge_by_distance = _decimate_planar.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = "ALL"
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Distance
    merge_by_distance.inputs[2].default_value = 0.0010000000474974513

    # node Reroute
    reroute = _decimate_planar.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketGeometry"
    # node Reroute.001
    reroute_001 = _decimate_planar.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketGeometry"
    # node Compare
    compare = _decimate_planar.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = "VECTOR"
    compare.mode = "DOT_PRODUCT"
    compare.operation = "LESS_THAN"
    # C
    compare.inputs[10].default_value = 0.0

    # node Normal
    normal = _decimate_planar.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"

    # node Position
    position = _decimate_planar.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    # node Normal.001
    normal_001 = _decimate_planar.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"

    # node Sample Nearest
    sample_nearest = _decimate_planar.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.domain = "FACE"

    # node Sample Index
    sample_index = _decimate_planar.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.clamp = False
    sample_index.data_type = "FLOAT_VECTOR"
    sample_index.domain = "FACE"

    # node Group Output
    group_output_1 = _decimate_planar.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    # node Reroute.002
    reroute_002 = _decimate_planar.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketGeometry"
    # node Mesh Line
    mesh_line = _decimate_planar.nodes.new("GeometryNodeMeshLine")
    mesh_line.name = "Mesh Line"
    mesh_line.count_mode = "TOTAL"
    mesh_line.mode = "OFFSET"
    mesh_line.inputs[1].hide = True
    mesh_line.inputs[2].hide = True
    # Start Location
    mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset
    mesh_line.inputs[3].default_value = (1.0, 0.0, 0.0)

    # node Domain Size
    domain_size = _decimate_planar.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size.name = "Domain Size"
    domain_size.component = "CURVE"
    domain_size.outputs[0].hide = True
    domain_size.outputs[1].hide = True
    domain_size.outputs[2].hide = True
    domain_size.outputs[3].hide = True
    domain_size.outputs[5].hide = True

    # node Sample Index.001
    sample_index_001 = _decimate_planar.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.clamp = False
    sample_index_001.data_type = "INT"
    sample_index_001.domain = "CURVE"

    # node Resample Curve
    resample_curve = _decimate_planar.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.mode = "COUNT"
    # Selection
    resample_curve.inputs[1].default_value = True

    # node Index
    index = _decimate_planar.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"

    # node Spline Length
    spline_length = _decimate_planar.nodes.new("GeometryNodeSplineLength")
    spline_length.name = "Spline Length"
    spline_length.outputs[0].hide = True

    # node Fill Curve
    fill_curve = _decimate_planar.nodes.new("GeometryNodeFillCurve")
    fill_curve.name = "Fill Curve"
    fill_curve.mode = "NGONS"
    # Group ID
    fill_curve.inputs[1].default_value = 0

    # node Sample Index.002
    sample_index_002 = _decimate_planar.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.clamp = False
    sample_index_002.data_type = "FLOAT_VECTOR"
    sample_index_002.domain = "POINT"

    # node Position.001
    position_001 = _decimate_planar.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    # node Index.001
    index_001 = _decimate_planar.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"

    # node Set Position
    set_position = _decimate_planar.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[1].hide = True
    set_position.inputs[3].hide = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Realize Instances
    realize_instances = _decimate_planar.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # node Instance on Points
    instance_on_points = _decimate_planar.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.inputs[1].hide = True
    instance_on_points.inputs[3].hide = True
    instance_on_points.inputs[4].hide = True
    instance_on_points.inputs[5].hide = True
    instance_on_points.inputs[6].hide = True
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    # node Reroute.003
    reroute_003 = _decimate_planar.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.socket_idname = "NodeSocketGeometry"
    # node Reroute.004
    reroute_004 = _decimate_planar.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketGeometry"
    # node Reroute.005
    reroute_005 = _decimate_planar.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketGeometry"
    # node Evaluate at Index
    evaluate_at_index = _decimate_planar.nodes.new("GeometryNodeFieldAtIndex")
    evaluate_at_index.name = "Evaluate at Index"
    evaluate_at_index.data_type = "FLOAT_VECTOR"
    evaluate_at_index.domain = "POINT"

    # node Evaluate at Index.001
    evaluate_at_index_001 = _decimate_planar.nodes.new("GeometryNodeFieldAtIndex")
    evaluate_at_index_001.name = "Evaluate at Index.001"
    evaluate_at_index_001.data_type = "FLOAT_VECTOR"
    evaluate_at_index_001.domain = "POINT"

    # node Edge Neighbors
    edge_neighbors = _decimate_planar.nodes.new("GeometryNodeInputMeshEdgeNeighbors")
    edge_neighbors.name = "Edge Neighbors"

    # node Compare.001
    compare_001 = _decimate_planar.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = "INT"
    compare_001.mode = "ELEMENT"
    compare_001.operation = "EQUAL"
    # B_INT
    compare_001.inputs[3].default_value = 0

    # node Compare.002
    compare_002 = _decimate_planar.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = "INT"
    compare_002.mode = "ELEMENT"
    compare_002.operation = "GREATER_THAN"
    # B_INT
    compare_002.inputs[3].default_value = 1

    # node Delete Geometry
    delete_geometry = _decimate_planar.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = "EDGE"
    delete_geometry.mode = "EDGE_FACE"

    # node Separate Geometry
    separate_geometry = _decimate_planar.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.domain = "EDGE"

    # node Reroute.006
    reroute_006 = _decimate_planar.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.socket_idname = "NodeSocketGeometry"
    # node Spline Parameter
    spline_parameter = _decimate_planar.nodes.new("GeometryNodeSplineParameter")
    spline_parameter.name = "Spline Parameter"
    spline_parameter.outputs[0].hide = True
    spline_parameter.outputs[1].hide = True

    # node Position.002
    position_002 = _decimate_planar.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"

    # node Math
    math_1 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = "SUBTRACT"
    math_1.use_clamp = False
    # Value_001
    math_1.inputs[1].default_value = 1.0

    # node Spline Length.001
    spline_length_001 = _decimate_planar.nodes.new("GeometryNodeSplineLength")
    spline_length_001.name = "Spline Length.001"
    spline_length_001.outputs[0].hide = True

    # node Math.001
    math_001_1 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = "ADD"
    math_001_1.use_clamp = False
    # Value_001
    math_001_1.inputs[1].default_value = 1.0

    # node Accumulate Field
    accumulate_field = _decimate_planar.nodes.new("GeometryNodeAccumulateField")
    accumulate_field.name = "Accumulate Field"
    accumulate_field.data_type = "INT"
    accumulate_field.domain = "CURVE"
    accumulate_field.inputs[1].hide = True
    accumulate_field.outputs[0].hide = True
    accumulate_field.outputs[2].hide = True
    # Group Index
    accumulate_field.inputs[1].default_value = 0

    # node Math.002
    math_002 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = "WRAP"
    math_002.use_clamp = False
    # Value_002
    math_002.inputs[2].default_value = 0.0

    # node Math.003
    math_003 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = "WRAP"
    math_003.use_clamp = False
    # Value_002
    math_003.inputs[2].default_value = 0.0

    # node Curve Circle
    curve_circle = _decimate_planar.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = "RADIUS"
    # Resolution
    curve_circle.inputs[0].default_value = 4
    # Radius
    curve_circle.inputs[4].default_value = 0.4000000059604645

    # node Reroute.007
    reroute_007 = _decimate_planar.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.socket_idname = "NodeSocketGeometry"
    # node Math.004
    math_004 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = "ADD"
    math_004.use_clamp = False

    # node Mesh to Curve
    mesh_to_curve = _decimate_planar.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.inputs[1].hide = True
    # Selection
    mesh_to_curve.inputs[1].default_value = True

    # node Math.005
    math_005 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = "ADD"
    math_005.use_clamp = False

    # node Position.003
    position_003 = _decimate_planar.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"

    # node Vector Math
    vector_math_1 = _decimate_planar.nodes.new("ShaderNodeVectorMath")
    vector_math_1.name = "Vector Math"
    vector_math_1.operation = "SUBTRACT"

    # node Vector Math.001
    vector_math_001_1 = _decimate_planar.nodes.new("ShaderNodeVectorMath")
    vector_math_001_1.name = "Vector Math.001"
    vector_math_001_1.operation = "SUBTRACT"

    # node Compare.003
    compare_003 = _decimate_planar.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = "VECTOR"
    compare_003.mode = "DIRECTION"
    compare_003.operation = "EQUAL"
    # Angle
    compare_003.inputs[11].default_value = 0.0
    # Epsilon
    compare_003.inputs[12].default_value = 0.0010000000474974513

    # node Delete Geometry.001
    delete_geometry_001 = _decimate_planar.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = "POINT"
    delete_geometry_001.mode = "ALL"

    # node Flip Faces
    flip_faces = _decimate_planar.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"

    # node Edge Angle
    edge_angle = _decimate_planar.nodes.new("GeometryNodeInputMeshEdgeAngle")
    edge_angle.name = "Edge Angle"
    edge_angle.outputs[1].hide = True

    # node Split Edges
    split_edges = _decimate_planar.nodes.new("GeometryNodeSplitEdges")
    split_edges.name = "Split Edges"

    # node Group Input
    group_input_1 = _decimate_planar.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    group_input_1.outputs[1].hide = True

    # node Compare.004
    compare_004 = _decimate_planar.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = "FLOAT"
    compare_004.mode = "ELEMENT"
    compare_004.operation = "NOT_EQUAL"
    # B
    compare_004.inputs[1].default_value = 0.0
    # Epsilon
    compare_004.inputs[12].default_value = 0.0010000000474974513

    # Set parents
    reroute_001.parent = frame
    compare.parent = frame
    normal.parent = frame
    position.parent = frame
    normal_001.parent = frame
    sample_nearest.parent = frame
    sample_index.parent = frame
    mesh_line.parent = frame_001
    domain_size.parent = frame_001
    sample_index_001.parent = frame_002
    resample_curve.parent = frame_002
    index.parent = frame_002
    spline_length.parent = frame_002
    fill_curve.parent = frame_002
    sample_index_002.parent = frame_004
    position_001.parent = frame_004
    index_001.parent = frame_004
    set_position.parent = frame_004
    realize_instances.parent = frame_003
    instance_on_points.parent = frame_003
    evaluate_at_index.parent = frame_006
    evaluate_at_index_001.parent = frame_006
    spline_parameter.parent = frame_007
    position_002.parent = frame_007
    math_1.parent = frame_007
    spline_length_001.parent = frame_007
    math_001_1.parent = frame_007
    accumulate_field.parent = frame_007
    math_002.parent = frame_007
    math_003.parent = frame_007
    curve_circle.parent = frame_003
    math_004.parent = frame_007
    math_005.parent = frame_007
    position_003.parent = frame_006
    vector_math_1.parent = frame_006
    vector_math_001_1.parent = frame_006
    compare_003.parent = frame_006
    delete_geometry_001.parent = frame_005
    edge_angle.parent = frame_008
    split_edges.parent = frame_008
    group_input_1.parent = frame_008
    compare_004.parent = frame_008

    # Set locations
    frame.location = (0.0, 20.0)
    frame_001.location = (-210.0, -137.0)
    frame_002.location = (0.0, 0.0)
    frame_003.location = (0.0, 0.0)
    frame_004.location = (40.0, 40.0)
    frame_005.location = (-370.0, 3.0)
    frame_006.location = (-390.0, 23.0)
    frame_007.location = (-490.0, 23.0)
    frame_008.location = (-450.0, 23.0)
    join_geometry.location = (-100.0, 60.0)
    merge_by_distance.location = (80.0, 60.0)
    reroute.location = (-200.0, 40.0)
    reroute_001.location = (-660.0, 160.0)
    compare.location = (80.0, 300.0)
    normal.location = (-100.0, 300.0)
    position.location = (-700.0, 300.21575927734375)
    normal_001.location = (-520.0, 140.0)
    sample_nearest.location = (-520.0, 300.0)
    sample_index.location = (-300.0, 300.0)
    group_output_1.location = (580.0, 140.0)
    reroute_002.location = (-2560.0, 180.0)
    mesh_line.location = (-1230.0, -163.0)
    domain_size.location = (-1410.0, -163.0)
    sample_index_001.location = (-860.0, -20.0)
    resample_curve.location = (-680.0, -20.0)
    index.location = (-1040.0, -80.0)
    spline_length.location = (-1040.0, -20.0)
    fill_curve.location = (-500.0, -20.0)
    sample_index_002.location = (-500.0, -340.0)
    position_001.location = (-680.0, -340.0)
    index_001.location = (-680.0, -400.0)
    set_position.location = (-320.0, -340.0)
    realize_instances.location = (-860.0, -300.0)
    instance_on_points.location = (-1040.0, -300.0)
    reroute_003.location = (-1620.0, -580.0)
    reroute_004.location = (-760.0, -580.0)
    reroute_005.location = (-1720.0, -380.0)
    evaluate_at_index.location = (-2110.0, -583.0)
    evaluate_at_index_001.location = (-2110.0, -403.0)
    edge_neighbors.location = (-2860.0, -160.0)
    compare_001.location = (-2680.0, -200.0)
    compare_002.location = (-2680.0, -80.0)
    delete_geometry.location = (-2500.0, 60.0)
    separate_geometry.location = (-2320.0, 0.0)
    reroute_006.location = (-2100.0, 40.0)
    spline_parameter.location = (-2810.0, -603.0)
    position_002.location = (-2250.0, -603.0)
    math_1.location = (-2630.0, -483.0)
    spline_length_001.location = (-2630.0, -603.0)
    math_001_1.location = (-2630.0, -663.0)
    accumulate_field.location = (-2430.0, -543.0)
    math_002.location = (-2430.0, -403.0)
    math_003.location = (-2430.0, -703.0)
    curve_circle.location = (-1220.0, -380.0)
    reroute_007.location = (-1620.0, -160.0)
    math_004.location = (-2250.0, -483.0)
    mesh_to_curve.location = (-2140.0, -240.0)
    math_005.location = (-2250.0, -663.0)
    position_003.location = (-1930.0, -563.0)
    vector_math_1.location = (-1930.0, -443.0)
    vector_math_001_1.location = (-1930.0, -623.0)
    compare_003.location = (-1750.0, -463.0)
    delete_geometry_001.location = (-1550.0, -263.0)
    flip_faces.location = (300.0, 140.0)
    edge_angle.location = (-2990.0, -65.5)
    split_edges.location = (-2610.0, -43.0)
    group_input_1.location = (-2800.0, 35.0)
    compare_004.location = (-2800.0, -32.0)

    # Set dimensions
    frame.width, frame.height = 980.0, 277.5
    frame_001.width, frame_001.height = 380.0, 254.5
    frame_002.width, frame_002.height = 740.0, 271.0
    frame_003.width, frame_003.height = 560.0, 279.0
    frame_004.width, frame_004.height = 560.0, 271.0
    frame_005.width, frame_005.height = 200.0, 219.5
    frame_006.width, frame_006.height = 560.0, 403.5
    frame_007.width, frame_007.height = 760.0, 486.5
    frame_008.width, frame_008.height = 580.0, 253.5
    join_geometry.width, join_geometry.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    reroute.width, reroute.height = 100.0, 100.0
    reroute_001.width, reroute_001.height = 100.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    normal_001.width, normal_001.height = 140.0, 100.0
    sample_nearest.width, sample_nearest.height = 140.0, 100.0
    sample_index.width, sample_index.height = 140.0, 100.0
    group_output_1.width, group_output_1.height = 140.0, 100.0
    reroute_002.width, reroute_002.height = 100.0, 100.0
    mesh_line.width, mesh_line.height = 140.0, 100.0
    domain_size.width, domain_size.height = 140.0, 100.0
    sample_index_001.width, sample_index_001.height = 140.0, 100.0
    resample_curve.width, resample_curve.height = 140.0, 100.0
    index.width, index.height = 140.0, 100.0
    spline_length.width, spline_length.height = 140.0, 100.0
    fill_curve.width, fill_curve.height = 140.0, 100.0
    sample_index_002.width, sample_index_002.height = 140.0, 100.0
    position_001.width, position_001.height = 140.0, 100.0
    index_001.width, index_001.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    reroute_003.width, reroute_003.height = 100.0, 100.0
    reroute_004.width, reroute_004.height = 100.0, 100.0
    reroute_005.width, reroute_005.height = 100.0, 100.0
    evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
    evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
    edge_neighbors.width, edge_neighbors.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    separate_geometry.width, separate_geometry.height = 140.0, 100.0
    reroute_006.width, reroute_006.height = 100.0, 100.0
    spline_parameter.width, spline_parameter.height = 140.0, 100.0
    position_002.width, position_002.height = 140.0, 100.0
    math_1.width, math_1.height = 140.0, 100.0
    spline_length_001.width, spline_length_001.height = 140.0, 100.0
    math_001_1.width, math_001_1.height = 140.0, 100.0
    accumulate_field.width, accumulate_field.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    curve_circle.width, curve_circle.height = 140.0, 100.0
    reroute_007.width, reroute_007.height = 100.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    position_003.width, position_003.height = 140.0, 100.0
    vector_math_1.width, vector_math_1.height = 140.0, 100.0
    vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
    flip_faces.width, flip_faces.height = 140.0, 100.0
    edge_angle.width, edge_angle.height = 140.0, 100.0
    split_edges.width, split_edges.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0

    # initialize _decimate_planar links
    # flip_faces.Mesh -> group_output_1.Geometry
    _decimate_planar.links.new(flip_faces.outputs[0], group_output_1.inputs[0])
    # edge_angle.Unsigned Angle -> compare_004.A
    _decimate_planar.links.new(edge_angle.outputs[0], compare_004.inputs[0])
    # group_input_1.Geometry -> split_edges.Mesh
    _decimate_planar.links.new(group_input_1.outputs[0], split_edges.inputs[0])
    # compare_004.Result -> split_edges.Selection
    _decimate_planar.links.new(compare_004.outputs[0], split_edges.inputs[1])
    # split_edges.Mesh -> delete_geometry.Geometry
    _decimate_planar.links.new(split_edges.outputs[0], delete_geometry.inputs[0])
    # edge_neighbors.Face Count -> compare_002.A
    _decimate_planar.links.new(edge_neighbors.outputs[0], compare_002.inputs[2])
    # compare_002.Result -> delete_geometry.Selection
    _decimate_planar.links.new(compare_002.outputs[0], delete_geometry.inputs[1])
    # edge_neighbors.Face Count -> compare_001.A
    _decimate_planar.links.new(edge_neighbors.outputs[0], compare_001.inputs[2])
    # separate_geometry.Selection -> mesh_to_curve.Mesh
    _decimate_planar.links.new(separate_geometry.outputs[0], mesh_to_curve.inputs[0])
    # delete_geometry.Geometry -> separate_geometry.Geometry
    _decimate_planar.links.new(delete_geometry.outputs[0], separate_geometry.inputs[0])
    # compare_001.Result -> separate_geometry.Selection
    _decimate_planar.links.new(compare_001.outputs[0], separate_geometry.inputs[1])
    # spline_parameter.Index -> math_001_1.Value
    _decimate_planar.links.new(spline_parameter.outputs[2], math_001_1.inputs[0])
    # math_001_1.Value -> math_003.Value
    _decimate_planar.links.new(math_001_1.outputs[0], math_003.inputs[0])
    # math_003.Value -> math_005.Value
    _decimate_planar.links.new(math_003.outputs[0], math_005.inputs[1])
    # spline_length_001.Point Count -> math_003.Value
    _decimate_planar.links.new(spline_length_001.outputs[1], math_003.inputs[1])
    # spline_length_001.Point Count -> accumulate_field.Value
    _decimate_planar.links.new(spline_length_001.outputs[1], accumulate_field.inputs[0])
    # accumulate_field.Trailing -> math_005.Value
    _decimate_planar.links.new(accumulate_field.outputs[1], math_005.inputs[0])
    # position_002.Position -> evaluate_at_index.Value
    _decimate_planar.links.new(position_002.outputs[0], evaluate_at_index.inputs[1])
    # math_005.Value -> evaluate_at_index.Index
    _decimate_planar.links.new(math_005.outputs[0], evaluate_at_index.inputs[0])
    # spline_parameter.Index -> math_1.Value
    _decimate_planar.links.new(spline_parameter.outputs[2], math_1.inputs[0])
    # math_1.Value -> math_002.Value
    _decimate_planar.links.new(math_1.outputs[0], math_002.inputs[0])
    # spline_length_001.Point Count -> math_002.Value
    _decimate_planar.links.new(spline_length_001.outputs[1], math_002.inputs[1])
    # math_002.Value -> math_004.Value
    _decimate_planar.links.new(math_002.outputs[0], math_004.inputs[0])
    # accumulate_field.Trailing -> math_004.Value
    _decimate_planar.links.new(accumulate_field.outputs[1], math_004.inputs[1])
    # math_004.Value -> evaluate_at_index_001.Index
    _decimate_planar.links.new(math_004.outputs[0], evaluate_at_index_001.inputs[0])
    # position_002.Position -> evaluate_at_index_001.Value
    _decimate_planar.links.new(position_002.outputs[0], evaluate_at_index_001.inputs[1])
    # position_003.Position -> vector_math_1.Vector
    _decimate_planar.links.new(position_003.outputs[0], vector_math_1.inputs[1])
    # evaluate_at_index_001.Value -> vector_math_1.Vector
    _decimate_planar.links.new(
        evaluate_at_index_001.outputs[0], vector_math_1.inputs[0]
    )
    # vector_math_1.Vector -> compare_003.A
    _decimate_planar.links.new(vector_math_1.outputs[0], compare_003.inputs[4])
    # vector_math_001_1.Vector -> compare_003.B
    _decimate_planar.links.new(vector_math_001_1.outputs[0], compare_003.inputs[5])
    # mesh_to_curve.Curve -> delete_geometry_001.Geometry
    _decimate_planar.links.new(mesh_to_curve.outputs[0], delete_geometry_001.inputs[0])
    # compare_003.Result -> delete_geometry_001.Selection
    _decimate_planar.links.new(compare_003.outputs[0], delete_geometry_001.inputs[1])
    # reroute_005.Output -> domain_size.Geometry
    _decimate_planar.links.new(reroute_005.outputs[0], domain_size.inputs[0])
    # position_001.Position -> sample_index_002.Value
    _decimate_planar.links.new(position_001.outputs[0], sample_index_002.inputs[1])
    # reroute_004.Output -> sample_index_002.Geometry
    _decimate_planar.links.new(reroute_004.outputs[0], sample_index_002.inputs[0])
    # sample_index_002.Value -> set_position.Position
    _decimate_planar.links.new(sample_index_002.outputs[0], set_position.inputs[2])
    # index_001.Index -> sample_index_002.Index
    _decimate_planar.links.new(index_001.outputs[0], sample_index_002.inputs[2])
    # set_position.Geometry -> join_geometry.Geometry
    _decimate_planar.links.new(set_position.outputs[0], join_geometry.inputs[0])
    # join_geometry.Geometry -> merge_by_distance.Geometry
    _decimate_planar.links.new(join_geometry.outputs[0], merge_by_distance.inputs[0])
    # separate_geometry.Inverted -> reroute_006.Input
    _decimate_planar.links.new(separate_geometry.outputs[1], reroute_006.inputs[0])
    # reroute_006.Output -> reroute.Input
    _decimate_planar.links.new(reroute_006.outputs[0], reroute.inputs[0])
    # reroute_001.Output -> sample_index.Geometry
    _decimate_planar.links.new(reroute_001.outputs[0], sample_index.inputs[0])
    # position.Position -> sample_nearest.Sample Position
    _decimate_planar.links.new(position.outputs[0], sample_nearest.inputs[1])
    # normal_001.Normal -> sample_index.Value
    _decimate_planar.links.new(normal_001.outputs[0], sample_index.inputs[1])
    # sample_nearest.Index -> sample_index.Index
    _decimate_planar.links.new(sample_nearest.outputs[0], sample_index.inputs[2])
    # reroute_001.Output -> sample_nearest.Geometry
    _decimate_planar.links.new(reroute_001.outputs[0], sample_nearest.inputs[0])
    # merge_by_distance.Geometry -> flip_faces.Mesh
    _decimate_planar.links.new(merge_by_distance.outputs[0], flip_faces.inputs[0])
    # compare.Result -> flip_faces.Selection
    _decimate_planar.links.new(compare.outputs[0], flip_faces.inputs[1])
    # normal.Normal -> compare.A
    _decimate_planar.links.new(normal.outputs[0], compare.inputs[4])
    # sample_index.Value -> compare.B
    _decimate_planar.links.new(sample_index.outputs[0], compare.inputs[5])
    # split_edges.Mesh -> reroute_002.Input
    _decimate_planar.links.new(split_edges.outputs[0], reroute_002.inputs[0])
    # reroute_002.Output -> reroute_001.Input
    _decimate_planar.links.new(reroute_002.outputs[0], reroute_001.inputs[0])
    # curve_circle.Curve -> instance_on_points.Instance
    _decimate_planar.links.new(curve_circle.outputs[0], instance_on_points.inputs[2])
    # mesh_line.Mesh -> instance_on_points.Points
    _decimate_planar.links.new(mesh_line.outputs[0], instance_on_points.inputs[0])
    # instance_on_points.Instances -> realize_instances.Geometry
    _decimate_planar.links.new(
        instance_on_points.outputs[0], realize_instances.inputs[0]
    )
    # realize_instances.Geometry -> resample_curve.Curve
    _decimate_planar.links.new(realize_instances.outputs[0], resample_curve.inputs[0])
    # reroute_007.Output -> sample_index_001.Geometry
    _decimate_planar.links.new(reroute_007.outputs[0], sample_index_001.inputs[0])
    # spline_length.Point Count -> sample_index_001.Value
    _decimate_planar.links.new(spline_length.outputs[1], sample_index_001.inputs[1])
    # index.Index -> sample_index_001.Index
    _decimate_planar.links.new(index.outputs[0], sample_index_001.inputs[2])
    # sample_index_001.Value -> resample_curve.Count
    _decimate_planar.links.new(sample_index_001.outputs[0], resample_curve.inputs[2])
    # fill_curve.Mesh -> set_position.Geometry
    _decimate_planar.links.new(fill_curve.outputs[0], set_position.inputs[0])
    # resample_curve.Curve -> fill_curve.Curve
    _decimate_planar.links.new(resample_curve.outputs[0], fill_curve.inputs[0])
    # domain_size.Spline Count -> mesh_line.Count
    _decimate_planar.links.new(domain_size.outputs[4], mesh_line.inputs[0])
    # reroute_005.Output -> reroute_003.Input
    _decimate_planar.links.new(reroute_005.outputs[0], reroute_003.inputs[0])
    # reroute_003.Output -> reroute_004.Input
    _decimate_planar.links.new(reroute_003.outputs[0], reroute_004.inputs[0])
    # delete_geometry_001.Geometry -> reroute_005.Input
    _decimate_planar.links.new(delete_geometry_001.outputs[0], reroute_005.inputs[0])
    # reroute_005.Output -> reroute_007.Input
    _decimate_planar.links.new(reroute_005.outputs[0], reroute_007.inputs[0])
    # position_003.Position -> vector_math_001_1.Vector
    _decimate_planar.links.new(position_003.outputs[0], vector_math_001_1.inputs[0])
    # evaluate_at_index.Value -> vector_math_001_1.Vector
    _decimate_planar.links.new(
        evaluate_at_index.outputs[0], vector_math_001_1.inputs[1]
    )
    # reroute.Output -> join_geometry.Geometry
    _decimate_planar.links.new(reroute.outputs[0], join_geometry.inputs[0])
    return _decimate_planar


_decimate_planar = _decimate_planar_node_group()


# initialize peg node group
def peg_node_group():
    peg = bpy.data.node_groups.new(type="GeometryNodeTree", name="Peg")

    peg.color_tag = "NONE"
    peg.description = ""
    peg.default_group_node_width = 140

    peg.is_modifier = True

    # peg interface
    # Socket Geometry
    geometry_socket_2 = peg.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket_2.attribute_domain = "POINT"

    # Socket random_seed
    random_seed_socket = peg.interface.new_socket(
        name="random_seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    random_seed_socket.default_value = 0
    random_seed_socket.min_value = 0
    random_seed_socket.max_value = 2147483647
    random_seed_socket.subtype = "NONE"
    random_seed_socket.attribute_domain = "POINT"

    # Socket profile_p_circle
    profile_p_circle_socket = peg.interface.new_socket(
        name="profile_p_circle", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    profile_p_circle_socket.default_value = 0.3333333432674408
    profile_p_circle_socket.min_value = 0.0
    profile_p_circle_socket.max_value = 1.0
    profile_p_circle_socket.subtype = "FACTOR"
    profile_p_circle_socket.attribute_domain = "POINT"

    # Socket profile_n_vertices_circle
    profile_n_vertices_circle_socket = peg.interface.new_socket(
        name="profile_n_vertices_circle", in_out="INPUT", socket_type="NodeSocketInt"
    )
    profile_n_vertices_circle_socket.default_value = 48
    profile_n_vertices_circle_socket.min_value = 3
    profile_n_vertices_circle_socket.max_value = 2147483647
    profile_n_vertices_circle_socket.subtype = "NONE"
    profile_n_vertices_circle_socket.attribute_domain = "POINT"

    # Socket profile_n_vertices_ngon_min
    profile_n_vertices_ngon_min_socket = peg.interface.new_socket(
        name="profile_n_vertices_ngon_min", in_out="INPUT", socket_type="NodeSocketInt"
    )
    profile_n_vertices_ngon_min_socket.default_value = 3
    profile_n_vertices_ngon_min_socket.min_value = 3
    profile_n_vertices_ngon_min_socket.max_value = 2147483647
    profile_n_vertices_ngon_min_socket.subtype = "NONE"
    profile_n_vertices_ngon_min_socket.attribute_domain = "POINT"

    # Socket profile_n_vertices_ngon_max
    profile_n_vertices_ngon_max_socket = peg.interface.new_socket(
        name="profile_n_vertices_ngon_max", in_out="INPUT", socket_type="NodeSocketInt"
    )
    profile_n_vertices_ngon_max_socket.default_value = 12
    profile_n_vertices_ngon_max_socket.min_value = 3
    profile_n_vertices_ngon_max_socket.max_value = 2147483647
    profile_n_vertices_ngon_max_socket.subtype = "NONE"
    profile_n_vertices_ngon_max_socket.attribute_domain = "POINT"

    # Socket radius_min
    radius_min_socket = peg.interface.new_socket(
        name="radius_min", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    radius_min_socket.default_value = 0.009999999776482582
    radius_min_socket.min_value = 0.0
    radius_min_socket.max_value = 3.4028234663852886e38
    radius_min_socket.subtype = "DISTANCE"
    radius_min_socket.attribute_domain = "POINT"

    # Socket radius_max
    radius_max_socket = peg.interface.new_socket(
        name="radius_max", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    radius_max_socket.default_value = 0.02500000037252903
    radius_max_socket.min_value = 0.0
    radius_max_socket.max_value = 3.4028234663852886e38
    radius_max_socket.subtype = "DISTANCE"
    radius_max_socket.attribute_domain = "POINT"

    # Socket height_min
    height_min_socket = peg.interface.new_socket(
        name="height_min", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    height_min_socket.default_value = 0.03999999910593033
    height_min_socket.min_value = 0.0
    height_min_socket.max_value = 3.4028234663852886e38
    height_min_socket.subtype = "DISTANCE"
    height_min_socket.attribute_domain = "POINT"

    # Socket height_max
    height_max_socket = peg.interface.new_socket(
        name="height_max", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    height_max_socket.default_value = 0.07999999821186066
    height_max_socket.min_value = 0.0
    height_max_socket.max_value = 3.4028234663852886e38
    height_max_socket.subtype = "DISTANCE"
    height_max_socket.attribute_domain = "POINT"

    # Socket aspect_ratio_min
    aspect_ratio_min_socket = peg.interface.new_socket(
        name="aspect_ratio_min", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    aspect_ratio_min_socket.default_value = 0.25
    aspect_ratio_min_socket.min_value = 0.0
    aspect_ratio_min_socket.max_value = 1.0
    aspect_ratio_min_socket.subtype = "FACTOR"
    aspect_ratio_min_socket.attribute_domain = "POINT"

    # Socket aspect_ratio_max
    aspect_ratio_max_socket = peg.interface.new_socket(
        name="aspect_ratio_max", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    aspect_ratio_max_socket.default_value = 1.0
    aspect_ratio_max_socket.min_value = 0.0
    aspect_ratio_max_socket.max_value = 1.0
    aspect_ratio_max_socket.subtype = "FACTOR"
    aspect_ratio_max_socket.attribute_domain = "POINT"

    # Socket taper_factor_min
    taper_factor_min_socket = peg.interface.new_socket(
        name="taper_factor_min", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    taper_factor_min_socket.default_value = 0.0
    taper_factor_min_socket.min_value = 0.0
    taper_factor_min_socket.max_value = 0.9990000128746033
    taper_factor_min_socket.subtype = "FACTOR"
    taper_factor_min_socket.attribute_domain = "POINT"

    # Socket taper_factor_max
    taper_factor_max_socket = peg.interface.new_socket(
        name="taper_factor_max", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    taper_factor_max_socket.default_value = 0.0
    taper_factor_max_socket.min_value = 0.0
    taper_factor_max_socket.max_value = 0.9990000128746033
    taper_factor_max_socket.subtype = "FACTOR"
    taper_factor_max_socket.attribute_domain = "POINT"

    # Socket use_uniform_geometry
    use_uniform_geometry_socket = peg.interface.new_socket(
        name="use_uniform_geometry", in_out="INPUT", socket_type="NodeSocketBool"
    )
    use_uniform_geometry_socket.default_value = False
    use_uniform_geometry_socket.attribute_domain = "POINT"

    # initialize peg nodes
    # node Frame
    frame_1 = peg.nodes.new("NodeFrame")
    frame_1.label = "Peg Profile (N-Gon/Circle)"
    frame_1.name = "Frame"
    frame_1.label_size = 20
    frame_1.shrink = True

    # node Frame.001
    frame_001_1 = peg.nodes.new("NodeFrame")
    frame_001_1.label = "Base geometry"
    frame_001_1.name = "Frame.001"
    frame_001_1.label_size = 20
    frame_001_1.shrink = True

    # node Frame.002
    frame_002_1 = peg.nodes.new("NodeFrame")
    frame_002_1.label = "Refine Shape (Aspect Ratio)"
    frame_002_1.name = "Frame.002"
    frame_002_1.label_size = 20
    frame_002_1.shrink = True

    # node Frame.003
    frame_003_1 = peg.nodes.new("NodeFrame")
    frame_003_1.label = "Peg Height"
    frame_003_1.name = "Frame.003"
    frame_003_1.label_size = 20
    frame_003_1.shrink = True

    # node Frame.004
    frame_004_1 = peg.nodes.new("NodeFrame")
    frame_004_1.label = "Peg Radius: top"
    frame_004_1.name = "Frame.004"
    frame_004_1.label_size = 20
    frame_004_1.shrink = True

    # node Frame.005
    frame_005_1 = peg.nodes.new("NodeFrame")
    frame_005_1.label = "Peg Radius: bottom (tapering)"
    frame_005_1.name = "Frame.005"
    frame_005_1.label_size = 20
    frame_005_1.shrink = True

    # node Frame.006
    frame_006_1 = peg.nodes.new("NodeFrame")
    frame_006_1.label = "Make the geometry uniform"
    frame_006_1.name = "Frame.006"
    frame_006_1.label_size = 20
    frame_006_1.shrink = True

    # node Switch
    switch = peg.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = "INT"

    # node Group Input
    group_input_2 = peg.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"
    group_input_2.outputs[1].hide = True
    group_input_2.outputs[2].hide = True
    group_input_2.outputs[3].hide = True
    group_input_2.outputs[4].hide = True
    group_input_2.outputs[5].hide = True
    group_input_2.outputs[6].hide = True
    group_input_2.outputs[7].hide = True
    group_input_2.outputs[8].hide = True
    group_input_2.outputs[9].hide = True
    group_input_2.outputs[10].hide = True
    group_input_2.outputs[11].hide = True
    group_input_2.outputs[12].hide = True
    group_input_2.outputs[13].hide = True
    group_input_2.outputs[14].hide = True

    # node Integer
    integer = peg.nodes.new("FunctionNodeInputInt")
    integer.name = "Integer"
    integer.integer = 0

    # node Group Input.001
    group_input_001 = peg.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True
    group_input_001.outputs[7].hide = True
    group_input_001.outputs[8].hide = True
    group_input_001.outputs[9].hide = True
    group_input_001.outputs[10].hide = True
    group_input_001.outputs[11].hide = True
    group_input_001.outputs[12].hide = True
    group_input_001.outputs[13].hide = True
    group_input_001.outputs[14].hide = True

    # node Random Value
    random_value = peg.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = "BOOLEAN"

    # node Group Input.002
    group_input_002 = peg.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True
    group_input_002.outputs[8].hide = True
    group_input_002.outputs[9].hide = True
    group_input_002.outputs[10].hide = True
    group_input_002.outputs[11].hide = True
    group_input_002.outputs[12].hide = True
    group_input_002.outputs[13].hide = True
    group_input_002.outputs[14].hide = True

    # node Random Value.001
    random_value_001 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = "INT"

    # node Group Input.003
    group_input_003 = peg.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[4].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[10].hide = True
    group_input_003.outputs[11].hide = True
    group_input_003.outputs[12].hide = True
    group_input_003.outputs[13].hide = True
    group_input_003.outputs[14].hide = True

    # node Integer.001
    integer_001 = peg.nodes.new("FunctionNodeInputInt")
    integer_001.name = "Integer.001"
    integer_001.integer = 1

    # node Group Input.004
    group_input_004 = peg.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True
    group_input_004.outputs[11].hide = True
    group_input_004.outputs[12].hide = True
    group_input_004.outputs[13].hide = True
    group_input_004.outputs[14].hide = True

    # node Reroute
    reroute_1 = peg.nodes.new("NodeReroute")
    reroute_1.label = "is_circle"
    reroute_1.name = "Reroute"
    reroute_1.socket_idname = "NodeSocketBool"
    # node Math
    math_2 = peg.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = "MULTIPLY"
    math_2.use_clamp = False
    math_2.inputs[0].hide = True
    math_2.inputs[2].hide = True
    # Value
    math_2.inputs[0].default_value = -0.5

    # node Combine XYZ
    combine_xyz_1 = peg.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_1.name = "Combine XYZ"
    combine_xyz_1.inputs[0].hide = True
    combine_xyz_1.inputs[1].hide = True
    # X
    combine_xyz_1.inputs[0].default_value = 0.0
    # Y
    combine_xyz_1.inputs[1].default_value = 0.0

    # node Scale Elements
    scale_elements = peg.nodes.new("GeometryNodeScaleElements")
    scale_elements.name = "Scale Elements"
    scale_elements.domain = "FACE"
    scale_elements.scale_mode = "SINGLE_AXIS"
    # Selection
    scale_elements.inputs[1].default_value = True
    # Center
    scale_elements.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Integer.002
    integer_002 = peg.nodes.new("FunctionNodeInputInt")
    integer_002.name = "Integer.002"
    integer_002.integer = 5

    # node Group Input.005
    group_input_005 = peg.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[6].hide = True
    group_input_005.outputs[7].hide = True
    group_input_005.outputs[8].hide = True
    group_input_005.outputs[9].hide = True
    group_input_005.outputs[10].hide = True
    group_input_005.outputs[11].hide = True
    group_input_005.outputs[12].hide = True
    group_input_005.outputs[13].hide = True
    group_input_005.outputs[14].hide = True

    # node Random Value.002
    random_value_002 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = "FLOAT"

    # node Group Input.006
    group_input_006 = peg.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[6].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True
    group_input_006.outputs[11].hide = True
    group_input_006.outputs[12].hide = True
    group_input_006.outputs[13].hide = True
    group_input_006.outputs[14].hide = True

    # node Random Value.003
    random_value_003 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_003.name = "Random Value.003"
    random_value_003.data_type = "FLOAT_VECTOR"
    # Min
    random_value_003.inputs[0].default_value = (-1.0, -1.0, 0.0)
    # Max
    random_value_003.inputs[1].default_value = (1.0, 1.0, 0.0)

    # node Group Input.007
    group_input_007 = peg.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[1].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[3].hide = True
    group_input_007.outputs[4].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[8].hide = True
    group_input_007.outputs[11].hide = True
    group_input_007.outputs[12].hide = True
    group_input_007.outputs[13].hide = True
    group_input_007.outputs[14].hide = True

    # node Group Output
    group_output_2 = peg.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True
    group_output_2.inputs[1].hide = True

    # node Set Shade Smooth
    set_shade_smooth = peg.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = "FACE"

    # node Integer.003
    integer_003 = peg.nodes.new("FunctionNodeInputInt")
    integer_003.name = "Integer.003"
    integer_003.integer = 6

    # node Transform Geometry
    transform_geometry = peg.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mute = True
    transform_geometry.mode = "COMPONENTS"
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[3].hide = True
    # Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Cone
    cone = peg.nodes.new("GeometryNodeMeshCone")
    cone.name = "Cone"
    cone.fill_type = "NGON"

    # node Group Input.008
    group_input_008 = peg.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[1].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[3].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[5].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True
    group_input_008.outputs[11].hide = True
    group_input_008.outputs[12].hide = True
    group_input_008.outputs[13].hide = True
    group_input_008.outputs[14].hide = True

    # node Integer.004
    integer_004 = peg.nodes.new("FunctionNodeInputInt")
    integer_004.name = "Integer.004"
    integer_004.integer = 3

    # node Group Input.009
    group_input_009 = peg.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"
    group_input_009.outputs[1].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[3].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[6].hide = True
    group_input_009.outputs[7].hide = True
    group_input_009.outputs[8].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True
    group_input_009.outputs[11].hide = True
    group_input_009.outputs[12].hide = True
    group_input_009.outputs[13].hide = True
    group_input_009.outputs[14].hide = True

    # node Random Value.004
    random_value_004 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_004.name = "Random Value.004"
    random_value_004.data_type = "FLOAT"

    # node Group Input.010
    group_input_010 = peg.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"
    group_input_010.outputs[1].hide = True
    group_input_010.outputs[2].hide = True
    group_input_010.outputs[3].hide = True
    group_input_010.outputs[4].hide = True
    group_input_010.outputs[5].hide = True
    group_input_010.outputs[6].hide = True
    group_input_010.outputs[7].hide = True
    group_input_010.outputs[8].hide = True
    group_input_010.outputs[9].hide = True
    group_input_010.outputs[10].hide = True
    group_input_010.outputs[11].hide = True
    group_input_010.outputs[12].hide = True
    group_input_010.outputs[13].hide = True
    group_input_010.outputs[14].hide = True

    # node Integer.005
    integer_005 = peg.nodes.new("FunctionNodeInputInt")
    integer_005.name = "Integer.005"
    integer_005.integer = 2

    # node Group Input.011
    group_input_011 = peg.nodes.new("NodeGroupInput")
    group_input_011.name = "Group Input.011"
    group_input_011.outputs[0].hide = True
    group_input_011.outputs[1].hide = True
    group_input_011.outputs[2].hide = True
    group_input_011.outputs[3].hide = True
    group_input_011.outputs[4].hide = True
    group_input_011.outputs[7].hide = True
    group_input_011.outputs[8].hide = True
    group_input_011.outputs[9].hide = True
    group_input_011.outputs[10].hide = True
    group_input_011.outputs[11].hide = True
    group_input_011.outputs[12].hide = True
    group_input_011.outputs[13].hide = True
    group_input_011.outputs[14].hide = True

    # node Random Value.005
    random_value_005 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_005.name = "Random Value.005"
    random_value_005.data_type = "FLOAT"

    # node Math.001
    math_001_2 = peg.nodes.new("ShaderNodeMath")
    math_001_2.name = "Math.001"
    math_001_2.operation = "SUBTRACT"
    math_001_2.use_clamp = False
    # Value
    math_001_2.inputs[0].default_value = 1.0

    # node Math.002
    math_002_1 = peg.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = "MULTIPLY"
    math_002_1.use_clamp = False

    # node Group Input.012
    group_input_012 = peg.nodes.new("NodeGroupInput")
    group_input_012.name = "Group Input.012"
    group_input_012.outputs[0].hide = True
    group_input_012.outputs[1].hide = True
    group_input_012.outputs[2].hide = True
    group_input_012.outputs[3].hide = True
    group_input_012.outputs[4].hide = True
    group_input_012.outputs[5].hide = True
    group_input_012.outputs[6].hide = True
    group_input_012.outputs[7].hide = True
    group_input_012.outputs[8].hide = True
    group_input_012.outputs[9].hide = True
    group_input_012.outputs[10].hide = True
    group_input_012.outputs[13].hide = True
    group_input_012.outputs[14].hide = True

    # node Integer.006
    integer_006 = peg.nodes.new("FunctionNodeInputInt")
    integer_006.name = "Integer.006"
    integer_006.integer = 4

    # node Group Input.013
    group_input_013 = peg.nodes.new("NodeGroupInput")
    group_input_013.name = "Group Input.013"
    group_input_013.outputs[1].hide = True
    group_input_013.outputs[2].hide = True
    group_input_013.outputs[3].hide = True
    group_input_013.outputs[4].hide = True
    group_input_013.outputs[5].hide = True
    group_input_013.outputs[6].hide = True
    group_input_013.outputs[7].hide = True
    group_input_013.outputs[8].hide = True
    group_input_013.outputs[9].hide = True
    group_input_013.outputs[10].hide = True
    group_input_013.outputs[11].hide = True
    group_input_013.outputs[12].hide = True
    group_input_013.outputs[13].hide = True
    group_input_013.outputs[14].hide = True

    # node Random Value.006
    random_value_006 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_006.name = "Random Value.006"
    random_value_006.data_type = "FLOAT"

    # node Reroute.001
    reroute_001_1 = peg.nodes.new("NodeReroute")
    reroute_001_1.label = "Radius"
    reroute_001_1.name = "Reroute.001"
    reroute_001_1.socket_idname = "NodeSocketFloat"
    # node Reroute.002
    reroute_002_1 = peg.nodes.new("NodeReroute")
    reroute_002_1.name = "Reroute.002"
    reroute_002_1.socket_idname = "NodeSocketInt"
    # node Reroute.003
    reroute_003_1 = peg.nodes.new("NodeReroute")
    reroute_003_1.label = "Vertices"
    reroute_003_1.name = "Reroute.003"
    reroute_003_1.socket_idname = "NodeSocketInt"
    # node Reroute.004
    reroute_004_1 = peg.nodes.new("NodeReroute")
    reroute_004_1.label = "Height"
    reroute_004_1.name = "Reroute.004"
    reroute_004_1.socket_idname = "NodeSocketFloat"
    # node Reroute.005
    reroute_005_1 = peg.nodes.new("NodeReroute")
    reroute_005_1.name = "Reroute.005"
    reroute_005_1.socket_idname = "NodeSocketFloat"
    # node Reroute.006
    reroute_006_1 = peg.nodes.new("NodeReroute")
    reroute_006_1.name = "Reroute.006"
    reroute_006_1.socket_idname = "NodeSocketFloat"
    # node Math.003
    math_003_1 = peg.nodes.new("ShaderNodeMath")
    math_003_1.name = "Math.003"
    math_003_1.operation = "DIVIDE"
    math_003_1.use_clamp = False

    # node Math.004
    math_004_1 = peg.nodes.new("ShaderNodeMath")
    math_004_1.name = "Math.004"
    math_004_1.operation = "DIVIDE"
    math_004_1.use_clamp = False

    # node Math.005
    math_005_1 = peg.nodes.new("ShaderNodeMath")
    math_005_1.name = "Math.005"
    math_005_1.operation = "CEIL"
    math_005_1.use_clamp = False

    # node Switch.001
    switch_001 = peg.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = "INT"
    # False
    switch_001.inputs[1].default_value = 1

    # node Math.006
    math_006 = peg.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = "CEIL"
    math_006.use_clamp = False

    # node Group Input.014
    group_input_014 = peg.nodes.new("NodeGroupInput")
    group_input_014.name = "Group Input.014"
    group_input_014.outputs[0].hide = True
    group_input_014.outputs[1].hide = True
    group_input_014.outputs[2].hide = True
    group_input_014.outputs[3].hide = True
    group_input_014.outputs[4].hide = True
    group_input_014.outputs[5].hide = True
    group_input_014.outputs[6].hide = True
    group_input_014.outputs[7].hide = True
    group_input_014.outputs[8].hide = True
    group_input_014.outputs[9].hide = True
    group_input_014.outputs[10].hide = True
    group_input_014.outputs[11].hide = True
    group_input_014.outputs[12].hide = True
    group_input_014.outputs[14].hide = True

    # node Switch.002
    switch_002 = peg.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.input_type = "INT"
    # False
    switch_002.inputs[1].default_value = 1

    # node Math.007
    math_007 = peg.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = "MULTIPLY"
    math_007.use_clamp = False
    # Value_001
    math_007.inputs[1].default_value = 6.2831854820251465

    # node Math.008
    math_008 = peg.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = "DIVIDE"
    math_008.use_clamp = False

    # node Reroute.007
    reroute_007_1 = peg.nodes.new("NodeReroute")
    reroute_007_1.label = "Circumference"
    reroute_007_1.name = "Reroute.007"
    reroute_007_1.socket_idname = "NodeSocketFloat"
    # node Reroute.008
    reroute_008 = peg.nodes.new("NodeReroute")
    reroute_008.label = "Vertex per meter"
    reroute_008.name = "Reroute.008"
    reroute_008.socket_idname = "NodeSocketFloat"
    # node Set Material
    set_material = peg.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    # Selection
    set_material.inputs[1].default_value = True
    if "Metal" in bpy.data.materials:
        set_material.inputs[2].default_value = bpy.data.materials["Metal"]

    # Set parents
    switch.parent = frame_1
    group_input_2.parent = frame_1
    integer.parent = frame_1
    group_input_001.parent = frame_1
    random_value.parent = frame_1
    group_input_002.parent = frame_1
    random_value_001.parent = frame_1
    group_input_003.parent = frame_1
    integer_001.parent = frame_1
    group_input_004.parent = frame_1
    math_2.parent = frame_001_1
    combine_xyz_1.parent = frame_001_1
    scale_elements.parent = frame_002_1
    integer_002.parent = frame_002_1
    group_input_005.parent = frame_002_1
    random_value_002.parent = frame_002_1
    group_input_006.parent = frame_002_1
    random_value_003.parent = frame_002_1
    group_input_007.parent = frame_002_1
    integer_003.parent = frame_002_1
    transform_geometry.parent = frame_001_1
    cone.parent = frame_001_1
    group_input_008.parent = frame_003_1
    integer_004.parent = frame_003_1
    group_input_009.parent = frame_003_1
    random_value_004.parent = frame_003_1
    group_input_010.parent = frame_004_1
    integer_005.parent = frame_004_1
    group_input_011.parent = frame_004_1
    random_value_005.parent = frame_005_1
    math_001_2.parent = frame_005_1
    math_002_1.parent = frame_005_1
    group_input_012.parent = frame_005_1
    integer_006.parent = frame_005_1
    group_input_013.parent = frame_005_1
    random_value_006.parent = frame_004_1
    math_003_1.parent = frame_006_1
    math_004_1.parent = frame_006_1
    math_005_1.parent = frame_006_1
    switch_001.parent = frame_006_1
    math_006.parent = frame_006_1
    group_input_014.parent = frame_006_1
    switch_002.parent = frame_006_1
    math_007.parent = frame_006_1
    math_008.parent = frame_006_1
    reroute_007_1.parent = frame_006_1
    reroute_008.parent = frame_006_1

    # Set locations
    frame_1.location = (-2364.13134765625, 475.01434326171875)
    frame_001_1.location = (757.2171020507812, 359.275146484375)
    frame_002_1.location = (1188.4765625, 284.1412353515625)
    frame_003_1.location = (-1824.343505859375, -462.14923095703125)
    frame_004_1.location = (-2608.612548828125, -299.5426025390625)
    frame_005_1.location = (-1215.678955078125, -47.47259521484375)
    frame_006_1.location = (-264.650146484375, 222.4400634765625)
    switch.location = (-237.70013427734375, 166.01531982421875)
    group_input_2.location = (-723.4949340820312, 200.67462158203125)
    integer.location = (-723.4949340820312, 295.67462158203125)
    group_input_001.location = (-723.4949340820312, 362.67462158203125)
    random_value.location = (-477.853759765625, 293.44110107421875)
    group_input_002.location = (-477.853759765625, -99.47715759277344)
    random_value_001.location = (-477.853759765625, 88.5228271484375)
    group_input_003.location = (-723.4949340820312, -93.69970703125)
    integer_001.location = (-723.4949340820312, 1.30029296875)
    group_input_004.location = (-723.4949340820312, 90.30029296875)
    reroute_1.location = (-201.34002685546875, 723.4322509765625)
    math_2.location = (-1397.6171875, -383.7940673828125)
    combine_xyz_1.location = (-1219.19677734375, -358.5167236328125)
    scale_elements.location = (-426.781494140625, 45.8795166015625)
    integer_002.location = (-891.415771484375, -128.57574462890625)
    group_input_005.location = (-891.415771484375, -223.57574462890625)
    random_value_002.location = (-645.774658203125, -79.97119140625)
    group_input_006.location = (-891.415771484375, -528.1066284179688)
    random_value_003.location = (-645.774658203125, -292.082275390625)
    group_input_007.location = (-891.415771484375, -39.57568359375)
    group_output_2.location = (1192.8258056640625, 334.2099914550781)
    set_shade_smooth.location = (41.69342041015625, 308.8958740234375)
    integer_003.location = (-891.415771484375, -433.10662841796875)
    transform_geometry.location = (-1027.566650390625, -12.72100830078125)
    cone.location = (-1400.453125, -39.529327392578125)
    group_input_008.location = (-891.415771484375, -175.932861328125)
    integer_004.location = (-891.415771484375, -264.932861328125)
    group_input_009.location = (-891.415771484375, -359.932861328125)
    random_value_004.location = (-645.7745971679688, -216.32830810546875)
    group_input_010.location = (-896.7049560546875, -34.74586486816406)
    integer_005.location = (-896.7049560546875, 60.25413513183594)
    group_input_011.location = (-896.7049560546875, 149.25413513183594)
    random_value_005.location = (-1479.693603515625, -280.1707763671875)
    math_001_2.location = (-1289.693603515625, -289.6707763671875)
    math_002_1.location = (-1059.5533447265625, -268.74444580078125)
    group_input_012.location = (-1669.693603515625, -242.329833984375)
    integer_006.location = (-1669.693603515625, -331.329833984375)
    group_input_013.location = (-1669.693603515625, -426.329833984375)
    random_value_006.location = (-651.063720703125, 105.62535095214844)
    reroute_001_1.location = (-2987.373046875, -228.5765380859375)
    reroute_002_1.location = (-974.951416015625, 606.3013305664062)
    reroute_003_1.location = (-2168.303466796875, 606.7763671875)
    reroute_004_1.location = (-2240.54443359375, -715.2064819335938)
    reroute_005_1.location = (-1903.29833984375, -714.4459838867188)
    reroute_006_1.location = (-2367.25, -228.5765380859375)
    math_003_1.location = (-1266.7904052734375, 298.87701416015625)
    math_004_1.location = (-1266.7904052734375, 34.935150146484375)
    math_005_1.location = (-1076.7904052734375, 287.87701416015625)
    switch_001.location = (-886.7904052734375, 298.37701416015625)
    math_006.location = (-1076.7904052734375, 23.935150146484375)
    group_input_014.location = (-1076.7904052734375, 113.1856689453125)
    switch_002.location = (-886.7904052734375, 34.435150146484375)
    math_007.location = (-1901.017578125, 42.23974609375)
    math_008.location = (-1586.1864013671875, 121.13839721679688)
    reroute_007_1.location = (-1719.8779296875, 7.324859619140625)
    reroute_008.location = (-1394.48095703125, 87.21310424804688)
    set_material.location = (1014.396484375, 335.28179931640625)

    # Set dimensions
    frame_1.width, frame_1.height = 686.0, 584.0
    frame_001_1.width, frame_001_1.height = 572.9999389648438, 568.0
    frame_002_1.width, frame_002_1.height = 665.0, 696.0
    frame_003_1.width, frame_003_1.height = 446.0, 306.0
    frame_004_1.width, frame_004_1.height = 445.0, 306.0
    frame_005_1.width, frame_005_1.height = 810.0, 306.0
    frame_006_1.width, frame_006_1.height = 1215.0, 482.0
    switch.width, switch.height = 140.0, 100.0
    group_input_2.width, group_input_2.height = 140.0, 100.0
    integer.width, integer.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    random_value.width, random_value.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    integer_001.width, integer_001.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    reroute_1.width, reroute_1.height = 16.0, 100.0
    math_2.width, math_2.height = 140.0, 100.0
    combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
    scale_elements.width, scale_elements.height = 140.0, 100.0
    integer_002.width, integer_002.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    random_value_003.width, random_value_003.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    group_output_2.width, group_output_2.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    integer_003.width, integer_003.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    cone.width, cone.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    integer_004.width, integer_004.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    random_value_004.width, random_value_004.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    integer_005.width, integer_005.height = 140.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    random_value_005.width, random_value_005.height = 140.0, 100.0
    math_001_2.width, math_001_2.height = 140.0, 100.0
    math_002_1.width, math_002_1.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    integer_006.width, integer_006.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    random_value_006.width, random_value_006.height = 140.0, 100.0
    reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
    reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
    reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
    reroute_004_1.width, reroute_004_1.height = 16.0, 100.0
    reroute_005_1.width, reroute_005_1.height = 16.0, 100.0
    reroute_006_1.width, reroute_006_1.height = 16.0, 100.0
    math_003_1.width, math_003_1.height = 140.0, 100.0
    math_004_1.width, math_004_1.height = 140.0, 100.0
    math_005_1.width, math_005_1.height = 140.0, 100.0
    switch_001.width, switch_001.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    switch_002.width, switch_002.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    reroute_007_1.width, reroute_007_1.height = 16.0, 100.0
    reroute_008.width, reroute_008.height = 16.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0

    # initialize peg links
    # group_input_003.random_seed -> random_value_001.Seed
    peg.links.new(group_input_003.outputs[0], random_value_001.inputs[8])
    # integer_001.Integer -> random_value_001.ID
    peg.links.new(integer_001.outputs[0], random_value_001.inputs[7])
    # group_input_2.random_seed -> random_value.Seed
    peg.links.new(group_input_2.outputs[0], random_value.inputs[8])
    # integer.Integer -> random_value.ID
    peg.links.new(integer.outputs[0], random_value.inputs[7])
    # random_value_001.Value -> switch.False
    peg.links.new(random_value_001.outputs[2], switch.inputs[1])
    # random_value.Value -> switch.Switch
    peg.links.new(random_value.outputs[3], switch.inputs[0])
    # integer_005.Integer -> random_value_006.ID
    peg.links.new(integer_005.outputs[0], random_value_006.inputs[7])
    # group_input_010.random_seed -> random_value_006.Seed
    peg.links.new(group_input_010.outputs[0], random_value_006.inputs[8])
    # integer_004.Integer -> random_value_004.ID
    peg.links.new(integer_004.outputs[0], random_value_004.inputs[7])
    # group_input_009.random_seed -> random_value_004.Seed
    peg.links.new(group_input_009.outputs[0], random_value_004.inputs[8])
    # group_input_011.radius_min -> random_value_006.Min
    peg.links.new(group_input_011.outputs[5], random_value_006.inputs[2])
    # group_input_008.height_min -> random_value_004.Min
    peg.links.new(group_input_008.outputs[7], random_value_004.inputs[2])
    # group_input_002.profile_n_vertices_circle -> switch.True
    peg.links.new(group_input_002.outputs[2], switch.inputs[2])
    # group_input_001.profile_p_circle -> random_value.Probability
    peg.links.new(group_input_001.outputs[1], random_value.inputs[6])
    # group_input_004.profile_n_vertices_ngon_min -> random_value_001.Min
    peg.links.new(group_input_004.outputs[3], random_value_001.inputs[4])
    # random_value.Value -> reroute_1.Input
    peg.links.new(random_value.outputs[3], reroute_1.inputs[0])
    # reroute_1.Output -> set_shade_smooth.Shade Smooth
    peg.links.new(reroute_1.outputs[0], set_shade_smooth.inputs[2])
    # transform_geometry.Geometry -> set_shade_smooth.Geometry
    peg.links.new(transform_geometry.outputs[0], set_shade_smooth.inputs[0])
    # math_001_2.Value -> math_002_1.Value
    peg.links.new(math_001_2.outputs[0], math_002_1.inputs[1])
    # math_002_1.Value -> cone.Radius Bottom
    peg.links.new(math_002_1.outputs[0], cone.inputs[4])
    # cone.Side -> set_shade_smooth.Selection
    peg.links.new(cone.outputs[3], set_shade_smooth.inputs[1])
    # cone.Mesh -> transform_geometry.Geometry
    peg.links.new(cone.outputs[0], transform_geometry.inputs[0])
    # combine_xyz_1.Vector -> transform_geometry.Translation
    peg.links.new(combine_xyz_1.outputs[0], transform_geometry.inputs[1])
    # math_2.Value -> combine_xyz_1.Z
    peg.links.new(math_2.outputs[0], combine_xyz_1.inputs[2])
    # random_value_004.Value -> reroute_004_1.Input
    peg.links.new(random_value_004.outputs[1], reroute_004_1.inputs[0])
    # reroute_005_1.Output -> math_2.Value
    peg.links.new(reroute_005_1.outputs[0], math_2.inputs[1])
    # reroute_005_1.Output -> cone.Depth
    peg.links.new(reroute_005_1.outputs[0], cone.inputs[5])
    # reroute_006_1.Output -> cone.Radius Top
    peg.links.new(reroute_006_1.outputs[0], cone.inputs[3])
    # random_value_006.Value -> reroute_001_1.Input
    peg.links.new(random_value_006.outputs[1], reroute_001_1.inputs[0])
    # switch.Output -> reroute_003_1.Input
    peg.links.new(switch.outputs[0], reroute_003_1.inputs[0])
    # reroute_002_1.Output -> cone.Vertices
    peg.links.new(reroute_002_1.outputs[0], cone.inputs[0])
    # reroute_006_1.Output -> math_002_1.Value
    peg.links.new(reroute_006_1.outputs[0], math_002_1.inputs[0])
    # set_material.Geometry -> group_output_2.Geometry
    peg.links.new(set_material.outputs[0], group_output_2.inputs[0])
    # integer_002.Integer -> random_value_002.ID
    peg.links.new(integer_002.outputs[0], random_value_002.inputs[7])
    # group_input_005.random_seed -> random_value_002.Seed
    peg.links.new(group_input_005.outputs[0], random_value_002.inputs[8])
    # group_input_007.aspect_ratio_min -> random_value_002.Min
    peg.links.new(group_input_007.outputs[9], random_value_002.inputs[2])
    # group_input_007.aspect_ratio_max -> random_value_002.Max
    peg.links.new(group_input_007.outputs[10], random_value_002.inputs[3])
    # group_input_008.height_max -> random_value_004.Max
    peg.links.new(group_input_008.outputs[8], random_value_004.inputs[3])
    # group_input_011.radius_max -> random_value_006.Max
    peg.links.new(group_input_011.outputs[6], random_value_006.inputs[3])
    # group_input_004.profile_n_vertices_ngon_max -> random_value_001.Max
    peg.links.new(group_input_004.outputs[4], random_value_001.inputs[5])
    # set_shade_smooth.Geometry -> scale_elements.Geometry
    peg.links.new(set_shade_smooth.outputs[0], scale_elements.inputs[0])
    # random_value_002.Value -> scale_elements.Scale
    peg.links.new(random_value_002.outputs[1], scale_elements.inputs[2])
    # integer_003.Integer -> random_value_003.ID
    peg.links.new(integer_003.outputs[0], random_value_003.inputs[7])
    # group_input_006.random_seed -> random_value_003.Seed
    peg.links.new(group_input_006.outputs[0], random_value_003.inputs[8])
    # random_value_003.Value -> scale_elements.Axis
    peg.links.new(random_value_003.outputs[0], scale_elements.inputs[4])
    # integer_006.Integer -> random_value_005.ID
    peg.links.new(integer_006.outputs[0], random_value_005.inputs[7])
    # group_input_013.random_seed -> random_value_005.Seed
    peg.links.new(group_input_013.outputs[0], random_value_005.inputs[8])
    # group_input_012.taper_factor_min -> random_value_005.Min
    peg.links.new(group_input_012.outputs[11], random_value_005.inputs[2])
    # group_input_012.taper_factor_max -> random_value_005.Max
    peg.links.new(group_input_012.outputs[12], random_value_005.inputs[3])
    # random_value_005.Value -> math_001_2.Value
    peg.links.new(random_value_005.outputs[1], math_001_2.inputs[1])
    # reroute_001_1.Output -> reroute_006_1.Input
    peg.links.new(reroute_001_1.outputs[0], reroute_006_1.inputs[0])
    # reroute_007_1.Output -> math_008.Value
    peg.links.new(reroute_007_1.outputs[0], math_008.inputs[0])
    # reroute_003_1.Output -> math_008.Value
    peg.links.new(reroute_003_1.outputs[0], math_008.inputs[1])
    # reroute_005_1.Output -> math_003_1.Value
    peg.links.new(reroute_005_1.outputs[0], math_003_1.inputs[0])
    # reroute_008.Output -> math_003_1.Value
    peg.links.new(reroute_008.outputs[0], math_003_1.inputs[1])
    # math_003_1.Value -> math_005_1.Value
    peg.links.new(math_003_1.outputs[0], math_005_1.inputs[0])
    # switch_001.Output -> cone.Side Segments
    peg.links.new(switch_001.outputs[0], cone.inputs[1])
    # reroute_008.Output -> math_004_1.Value
    peg.links.new(reroute_008.outputs[0], math_004_1.inputs[1])
    # math_004_1.Value -> math_006.Value
    peg.links.new(math_004_1.outputs[0], math_006.inputs[0])
    # math_005_1.Value -> switch_001.True
    peg.links.new(math_005_1.outputs[0], switch_001.inputs[2])
    # math_006.Value -> switch_002.True
    peg.links.new(math_006.outputs[0], switch_002.inputs[2])
    # switch_002.Output -> cone.Fill Segments
    peg.links.new(switch_002.outputs[0], cone.inputs[2])
    # group_input_014.use_uniform_geometry -> switch_001.Switch
    peg.links.new(group_input_014.outputs[13], switch_001.inputs[0])
    # group_input_014.use_uniform_geometry -> switch_002.Switch
    peg.links.new(group_input_014.outputs[13], switch_002.inputs[0])
    # reroute_003_1.Output -> reroute_002_1.Input
    peg.links.new(reroute_003_1.outputs[0], reroute_002_1.inputs[0])
    # math_007.Value -> reroute_007_1.Input
    peg.links.new(math_007.outputs[0], reroute_007_1.inputs[0])
    # reroute_006_1.Output -> math_007.Value
    peg.links.new(reroute_006_1.outputs[0], math_007.inputs[0])
    # reroute_006_1.Output -> math_004_1.Value
    peg.links.new(reroute_006_1.outputs[0], math_004_1.inputs[0])
    # reroute_004_1.Output -> reroute_005_1.Input
    peg.links.new(reroute_004_1.outputs[0], reroute_005_1.inputs[0])
    # math_008.Value -> reroute_008.Input
    peg.links.new(math_008.outputs[0], reroute_008.inputs[0])
    # scale_elements.Geometry -> set_material.Geometry
    peg.links.new(scale_elements.outputs[0], set_material.inputs[0])
    return peg


peg = peg_node_group()


# initialize hole node group
def hole_node_group():
    hole = bpy.data.node_groups.new(type="GeometryNodeTree", name="Hole")

    hole.color_tag = "NONE"
    hole.description = ""
    hole.default_group_node_width = 140

    hole.is_modifier = True

    # hole interface
    # Socket Geometry
    geometry_socket_3 = hole.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket_3.attribute_domain = "POINT"

    # Socket entrance_position
    entrance_position_socket = hole.interface.new_socket(
        name="entrance_position", in_out="OUTPUT", socket_type="NodeSocketVector"
    )
    entrance_position_socket.default_value = (0.0, 0.0, 0.0)
    entrance_position_socket.min_value = -3.4028234663852886e38
    entrance_position_socket.max_value = 3.4028234663852886e38
    entrance_position_socket.subtype = "XYZ"
    entrance_position_socket.attribute_domain = "POINT"

    # Socket entrance_orientation
    entrance_orientation_socket = hole.interface.new_socket(
        name="entrance_orientation", in_out="OUTPUT", socket_type="NodeSocketVector"
    )
    entrance_orientation_socket.default_value = (0.0, 0.0, 0.0)
    entrance_orientation_socket.min_value = -3.4028234663852886e38
    entrance_orientation_socket.max_value = 3.4028234663852886e38
    entrance_orientation_socket.subtype = "EULER"
    entrance_orientation_socket.attribute_domain = "POINT"

    # Socket bottom_position
    bottom_position_socket = hole.interface.new_socket(
        name="bottom_position", in_out="OUTPUT", socket_type="NodeSocketVector"
    )
    bottom_position_socket.default_value = (0.0, 0.0, 0.0)
    bottom_position_socket.min_value = -3.4028234663852886e38
    bottom_position_socket.max_value = 3.4028234663852886e38
    bottom_position_socket.subtype = "XYZ"
    bottom_position_socket.attribute_domain = "POINT"

    # Socket bottom_orientation
    bottom_orientation_socket = hole.interface.new_socket(
        name="bottom_orientation", in_out="OUTPUT", socket_type="NodeSocketVector"
    )
    bottom_orientation_socket.default_value = (0.0, 0.0, 0.0)
    bottom_orientation_socket.min_value = -3.4028234663852886e38
    bottom_orientation_socket.max_value = 3.4028234663852886e38
    bottom_orientation_socket.subtype = "EULER"
    bottom_orientation_socket.attribute_domain = "POINT"

    # Socket Geometry
    geometry_socket_4 = hole.interface.new_socket(
        name="Geometry", in_out="INPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket_4.attribute_domain = "POINT"

    # Socket random_seed
    random_seed_socket_1 = hole.interface.new_socket(
        name="random_seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    random_seed_socket_1.default_value = 0
    random_seed_socket_1.min_value = 0
    random_seed_socket_1.max_value = 2147483647
    random_seed_socket_1.subtype = "NONE"
    random_seed_socket_1.attribute_domain = "POINT"

    # Socket peg
    peg_socket = hole.interface.new_socket(
        name="peg", in_out="INPUT", socket_type="NodeSocketObject"
    )
    peg_socket.attribute_domain = "POINT"

    # Socket hole_position_handle
    hole_position_handle_socket = hole.interface.new_socket(
        name="hole_position_handle", in_out="INPUT", socket_type="NodeSocketObject"
    )
    hole_position_handle_socket.attribute_domain = "POINT"

    # Socket hole_position_offset_min
    hole_position_offset_min_socket = hole.interface.new_socket(
        name="hole_position_offset_min", in_out="INPUT", socket_type="NodeSocketVector"
    )
    hole_position_offset_min_socket.default_value = (
        -0.05000000074505806,
        -0.05000000074505806,
        -0.05000000074505806,
    )
    hole_position_offset_min_socket.min_value = -3.4028234663852886e38
    hole_position_offset_min_socket.max_value = 3.4028234663852886e38
    hole_position_offset_min_socket.subtype = "TRANSLATION"
    hole_position_offset_min_socket.attribute_domain = "POINT"

    # Socket hole_position_offset_max
    hole_position_offset_max_socket = hole.interface.new_socket(
        name="hole_position_offset_max", in_out="INPUT", socket_type="NodeSocketVector"
    )
    hole_position_offset_max_socket.default_value = (
        0.05000000074505806,
        0.05000000074505806,
        0.05000000074505806,
    )
    hole_position_offset_max_socket.min_value = -3.4028234663852886e38
    hole_position_offset_max_socket.max_value = 3.4028234663852886e38
    hole_position_offset_max_socket.subtype = "TRANSLATION"
    hole_position_offset_max_socket.attribute_domain = "POINT"

    # Socket hole_orientation_offset_min
    hole_orientation_offset_min_socket = hole.interface.new_socket(
        name="hole_orientation_offset_min",
        in_out="INPUT",
        socket_type="NodeSocketVector",
    )
    hole_orientation_offset_min_socket.default_value = (
        -0.34906598925590515,
        -0.34906598925590515,
        -3.1415927410125732,
    )
    hole_orientation_offset_min_socket.min_value = -3.4028234663852886e38
    hole_orientation_offset_min_socket.max_value = 3.4028234663852886e38
    hole_orientation_offset_min_socket.subtype = "EULER"
    hole_orientation_offset_min_socket.attribute_domain = "POINT"

    # Socket hole_orientation_offset_max
    hole_orientation_offset_max_socket = hole.interface.new_socket(
        name="hole_orientation_offset_max",
        in_out="INPUT",
        socket_type="NodeSocketVector",
    )
    hole_orientation_offset_max_socket.default_value = (
        0.34906598925590515,
        0.34906598925590515,
        3.1415927410125732,
    )
    hole_orientation_offset_max_socket.min_value = -3.4028234663852886e38
    hole_orientation_offset_max_socket.max_value = 3.4028234663852886e38
    hole_orientation_offset_max_socket.subtype = "EULER"
    hole_orientation_offset_max_socket.attribute_domain = "POINT"

    # Socket hole_insertion_angle_min
    hole_insertion_angle_min_socket = hole.interface.new_socket(
        name="hole_insertion_angle_min", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    hole_insertion_angle_min_socket.default_value = 0.0
    hole_insertion_angle_min_socket.min_value = -3.4028234663852886e38
    hole_insertion_angle_min_socket.max_value = 3.4028234663852886e38
    hole_insertion_angle_min_socket.subtype = "ANGLE"
    hole_insertion_angle_min_socket.attribute_domain = "POINT"

    # Socket hole_insertion_angle_max
    hole_insertion_angle_max_socket = hole.interface.new_socket(
        name="hole_insertion_angle_max", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    hole_insertion_angle_max_socket.default_value = 6.2831854820251465
    hole_insertion_angle_max_socket.min_value = -3.4028234663852886e38
    hole_insertion_angle_max_socket.max_value = 3.4028234663852886e38
    hole_insertion_angle_max_socket.subtype = "ANGLE"
    hole_insertion_angle_max_socket.attribute_domain = "POINT"

    # Socket hole_depth_factor_min
    hole_depth_factor_min_socket = hole.interface.new_socket(
        name="hole_depth_factor_min", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    hole_depth_factor_min_socket.default_value = 0.25
    hole_depth_factor_min_socket.min_value = 0.0
    hole_depth_factor_min_socket.max_value = 1.0
    hole_depth_factor_min_socket.subtype = "FACTOR"
    hole_depth_factor_min_socket.attribute_domain = "POINT"

    # Socket hole_depth_factor_max
    hole_depth_factor_max_socket = hole.interface.new_socket(
        name="hole_depth_factor_max", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    hole_depth_factor_max_socket.default_value = 0.75
    hole_depth_factor_max_socket.min_value = 0.0
    hole_depth_factor_max_socket.max_value = 1.0
    hole_depth_factor_max_socket.subtype = "FACTOR"
    hole_depth_factor_max_socket.attribute_domain = "POINT"

    # Socket hole_size_tolerance
    hole_size_tolerance_socket = hole.interface.new_socket(
        name="hole_size_tolerance", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    hole_size_tolerance_socket.default_value = 0.0010000000474974513
    hole_size_tolerance_socket.min_value = 0.0
    hole_size_tolerance_socket.max_value = 3.4028234663852886e38
    hole_size_tolerance_socket.subtype = "DISTANCE"
    hole_size_tolerance_socket.attribute_domain = "POINT"

    # Socket wall_enable
    wall_enable_socket = hole.interface.new_socket(
        name="wall_enable", in_out="INPUT", socket_type="NodeSocketBool"
    )
    wall_enable_socket.default_value = True
    wall_enable_socket.attribute_domain = "POINT"

    # Socket wall_remove_inner_holes
    wall_remove_inner_holes_socket = hole.interface.new_socket(
        name="wall_remove_inner_holes", in_out="INPUT", socket_type="NodeSocketBool"
    )
    wall_remove_inner_holes_socket.default_value = False
    wall_remove_inner_holes_socket.attribute_domain = "POINT"

    # Socket wall_thickness
    wall_thickness_socket = hole.interface.new_socket(
        name="wall_thickness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    wall_thickness_socket.default_value = 0.005000000353902578
    wall_thickness_socket.min_value = 9.999999747378752e-05
    wall_thickness_socket.max_value = 10000.0
    wall_thickness_socket.subtype = "DISTANCE"
    wall_thickness_socket.attribute_domain = "POINT"

    # Socket wall_include_bottom
    wall_include_bottom_socket = hole.interface.new_socket(
        name="wall_include_bottom", in_out="INPUT", socket_type="NodeSocketBool"
    )
    wall_include_bottom_socket.default_value = True
    wall_include_bottom_socket.attribute_domain = "POINT"

    # initialize hole nodes
    # node Frame.001
    frame_001_2 = hole.nodes.new("NodeFrame")
    frame_001_2.label = "Add wall around the hole into the original geometry"
    frame_001_2.name = "Frame.001"
    frame_001_2.use_custom_color = True
    frame_001_2.color = (0.1600000113248825, 0.17599999904632568, 0.20000000298023224)
    frame_001_2.label_size = 20
    frame_001_2.shrink = True

    # node Frame.002
    frame_002_2 = hole.nodes.new("NodeFrame")
    frame_002_2.label = "Get and process peg geometry to form the hole"
    frame_002_2.name = "Frame.002"
    frame_002_2.use_custom_color = True
    frame_002_2.color = (0.16862745583057404, 0.20000001788139343, 0.16078431904315948)
    frame_002_2.label_size = 20
    frame_002_2.shrink = True

    # node Frame.003
    frame_003_2 = hole.nodes.new("NodeFrame")
    frame_003_2.label = "Get peg geometry positioned and oriented above the hole"
    frame_003_2.name = "Frame.003"
    frame_003_2.label_size = 20
    frame_003_2.shrink = True

    # node Frame.004
    frame_004_2 = hole.nodes.new("NodeFrame")
    frame_004_2.label = "Translate peg geometry into the inserted pose"
    frame_004_2.name = "Frame.004"
    frame_004_2.label_size = 20
    frame_004_2.shrink = True

    # node Frame.005
    frame_005_2 = hole.nodes.new("NodeFrame")
    frame_005_2.label = "Extend the top of the peg"
    frame_005_2.name = "Frame.005"
    frame_005_2.label_size = 20
    frame_005_2.shrink = True

    # node Frame.006
    frame_006_2 = hole.nodes.new("NodeFrame")
    frame_006_2.label = "Hole: Add tolerance to the size of the peg"
    frame_006_2.name = "Frame.006"
    frame_006_2.label_size = 20
    frame_006_2.shrink = True

    # node Frame.007
    frame_007_1 = hole.nodes.new("NodeFrame")
    frame_007_1.label = "Get (random) origin and direction of the hole"
    frame_007_1.name = "Frame.007"
    frame_007_1.label_size = 20
    frame_007_1.shrink = True

    # node Frame.008
    frame_008_1 = hole.nodes.new("NodeFrame")
    frame_008_1.label = "Get peg geometry that is randomly rotated around its Z axis"
    frame_008_1.name = "Frame.008"
    frame_008_1.label_size = 20
    frame_008_1.shrink = True

    # node Frame.009
    frame_009 = hole.nodes.new("NodeFrame")
    frame_009.label = "(Experimental) Support pegs with holes in the middle"
    frame_009.name = "Frame.009"
    frame_009.label_size = 20
    frame_009.shrink = True

    # node Frame.010
    frame_010 = hole.nodes.new("NodeFrame")
    frame_010.label = "TODO: Find a better way of remove inner holes from pegs"
    frame_010.name = "Frame.010"
    frame_010.label_size = 20
    frame_010.shrink = True

    # node Frame.011
    frame_011 = hole.nodes.new("NodeFrame")
    frame_011.label = "Walls: Add tolerance and wall width to the size of the peg"
    frame_011.name = "Frame.011"
    frame_011.label_size = 20
    frame_011.shrink = True

    # node Frame.012
    frame_012 = hole.nodes.new("NodeFrame")
    frame_012.label = "Add bottom portion to the wall geometry"
    frame_012.name = "Frame.012"
    frame_012.label_size = 20
    frame_012.shrink = True

    # node Frame.013
    frame_013 = hole.nodes.new("NodeFrame")
    frame_013.label = "Remove extra geometry from the walls above the hole"
    frame_013.name = "Frame.013"
    frame_013.label_size = 20
    frame_013.shrink = True

    # node Frame.014
    frame_014 = hole.nodes.new("NodeFrame")
    frame_014.label = "Merge original geometry with the walls"
    frame_014.name = "Frame.014"
    frame_014.label_size = 20
    frame_014.shrink = True

    # node Frame
    frame_2 = hole.nodes.new("NodeFrame")
    frame_2.label = "Remove hole for the peg"
    frame_2.name = "Frame"
    frame_2.label_size = 20
    frame_2.shrink = True

    # node Reroute
    reroute_2 = hole.nodes.new("NodeReroute")
    reroute_2.label = "peg_pull_direction"
    reroute_2.name = "Reroute"
    reroute_2.socket_idname = "NodeSocketVector"
    # node Reroute.001
    reroute_001_2 = hole.nodes.new("NodeReroute")
    reroute_001_2.label = "hole_position"
    reroute_001_2.name = "Reroute.001"
    reroute_001_2.socket_idname = "NodeSocketVector"
    # node Reroute.002
    reroute_002_2 = hole.nodes.new("NodeReroute")
    reroute_002_2.name = "Reroute.002"
    reroute_002_2.socket_idname = "NodeSocketVector"
    # node Reroute.003
    reroute_003_2 = hole.nodes.new("NodeReroute")
    reroute_003_2.label = "hole_position"
    reroute_003_2.name = "Reroute.003"
    reroute_003_2.socket_idname = "NodeSocketVector"
    # node Reroute.006
    reroute_006_2 = hole.nodes.new("NodeReroute")
    reroute_006_2.name = "Reroute.006"
    reroute_006_2.socket_idname = "NodeSocketVector"
    # node Reroute.007
    reroute_007_2 = hole.nodes.new("NodeReroute")
    reroute_007_2.label = "peg_insert_direction"
    reroute_007_2.name = "Reroute.007"
    reroute_007_2.socket_idname = "NodeSocketVector"
    # node Reroute.008
    reroute_008_1 = hole.nodes.new("NodeReroute")
    reroute_008_1.label = "peg_pull_direction"
    reroute_008_1.name = "Reroute.008"
    reroute_008_1.socket_idname = "NodeSocketVector"
    # node Group Input.001
    group_input_001_1 = hole.nodes.new("NodeGroupInput")
    group_input_001_1.name = "Group Input.001"
    group_input_001_1.outputs[0].hide = True
    group_input_001_1.outputs[1].hide = True
    group_input_001_1.outputs[3].hide = True
    group_input_001_1.outputs[4].hide = True
    group_input_001_1.outputs[5].hide = True
    group_input_001_1.outputs[6].hide = True
    group_input_001_1.outputs[7].hide = True
    group_input_001_1.outputs[8].hide = True
    group_input_001_1.outputs[9].hide = True
    group_input_001_1.outputs[10].hide = True
    group_input_001_1.outputs[11].hide = True
    group_input_001_1.outputs[12].hide = True
    group_input_001_1.outputs[13].hide = True
    group_input_001_1.outputs[14].hide = True
    group_input_001_1.outputs[15].hide = True
    group_input_001_1.outputs[16].hide = True
    group_input_001_1.outputs[17].hide = True

    # node Position
    position_1 = hole.nodes.new("GeometryNodeInputPosition")
    position_1.name = "Position"

    # node Object Info
    object_info = hole.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.transform_space = "ORIGINAL"
    object_info.inputs[1].hide = True
    object_info.outputs[1].hide = True
    object_info.outputs[2].hide = True
    object_info.outputs[3].hide = True
    # As Instance
    object_info.inputs[1].default_value = False

    # node Attribute Statistic
    attribute_statistic = hole.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.data_type = "FLOAT_VECTOR"
    attribute_statistic.domain = "POINT"
    attribute_statistic.inputs[1].hide = True
    attribute_statistic.outputs[0].hide = True
    attribute_statistic.outputs[1].hide = True
    attribute_statistic.outputs[2].hide = True
    attribute_statistic.outputs[4].hide = True
    attribute_statistic.outputs[6].hide = True
    attribute_statistic.outputs[7].hide = True
    # Selection
    attribute_statistic.inputs[1].default_value = True

    # node Vector Math
    vector_math_2 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_2.name = "Vector Math"
    vector_math_2.operation = "MULTIPLY"
    # Vector_001
    vector_math_2.inputs[1].default_value = (0.0, 0.0, -1.0)

    # node Align Euler to Vector
    align_euler_to_vector = hole.nodes.new("FunctionNodeAlignEulerToVector")
    align_euler_to_vector.name = "Align Euler to Vector"
    align_euler_to_vector.axis = "Z"
    align_euler_to_vector.pivot_axis = "AUTO"
    align_euler_to_vector.inputs[0].hide = True
    align_euler_to_vector.inputs[1].hide = True
    # Rotation
    align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Factor
    align_euler_to_vector.inputs[1].default_value = 1.0

    # node Reroute.009
    reroute_009 = hole.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.socket_idname = "NodeSocketVector"
    # node Separate XYZ
    separate_xyz_1 = hole.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_1.name = "Separate XYZ"
    separate_xyz_1.outputs[0].hide = True
    separate_xyz_1.outputs[1].hide = True

    # node Vector Rotate
    vector_rotate = hole.nodes.new("ShaderNodeVectorRotate")
    vector_rotate.name = "Vector Rotate"
    vector_rotate.invert = False
    vector_rotate.rotation_type = "EULER_XYZ"
    vector_rotate.inputs[1].hide = True
    vector_rotate.inputs[2].hide = True
    vector_rotate.inputs[3].hide = True
    # Center
    vector_rotate.inputs[1].default_value = (0.0, 0.0, 0.0)

    # node Vector Math.001
    vector_math_001_2 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_001_2.name = "Vector Math.001"
    vector_math_001_2.operation = "ADD"

    # node Reroute.010
    reroute_010 = hole.nodes.new("NodeReroute")
    reroute_010.label = "peg_height"
    reroute_010.name = "Reroute.010"
    reroute_010.socket_idname = "NodeSocketFloat"
    # node Transform Geometry
    transform_geometry_1 = hole.nodes.new("GeometryNodeTransform")
    transform_geometry_1.name = "Transform Geometry"
    transform_geometry_1.mode = "COMPONENTS"
    transform_geometry_1.inputs[3].hide = True
    # Scale
    transform_geometry_1.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Group Input.002
    group_input_002_1 = hole.nodes.new("NodeGroupInput")
    group_input_002_1.name = "Group Input.002"
    group_input_002_1.outputs[0].hide = True
    group_input_002_1.outputs[2].hide = True
    group_input_002_1.outputs[3].hide = True
    group_input_002_1.outputs[4].hide = True
    group_input_002_1.outputs[5].hide = True
    group_input_002_1.outputs[6].hide = True
    group_input_002_1.outputs[7].hide = True
    group_input_002_1.outputs[8].hide = True
    group_input_002_1.outputs[9].hide = True
    group_input_002_1.outputs[10].hide = True
    group_input_002_1.outputs[11].hide = True
    group_input_002_1.outputs[12].hide = True
    group_input_002_1.outputs[13].hide = True
    group_input_002_1.outputs[14].hide = True
    group_input_002_1.outputs[15].hide = True
    group_input_002_1.outputs[16].hide = True
    group_input_002_1.outputs[17].hide = True

    # node Random Value
    random_value_1 = hole.nodes.new("FunctionNodeRandomValue")
    random_value_1.name = "Random Value"
    random_value_1.data_type = "FLOAT"

    # node Group Input.003
    group_input_003_1 = hole.nodes.new("NodeGroupInput")
    group_input_003_1.name = "Group Input.003"
    group_input_003_1.outputs[0].hide = True
    group_input_003_1.outputs[1].hide = True
    group_input_003_1.outputs[2].hide = True
    group_input_003_1.outputs[3].hide = True
    group_input_003_1.outputs[4].hide = True
    group_input_003_1.outputs[5].hide = True
    group_input_003_1.outputs[6].hide = True
    group_input_003_1.outputs[7].hide = True
    group_input_003_1.outputs[8].hide = True
    group_input_003_1.outputs[9].hide = True
    group_input_003_1.outputs[12].hide = True
    group_input_003_1.outputs[13].hide = True
    group_input_003_1.outputs[14].hide = True
    group_input_003_1.outputs[15].hide = True
    group_input_003_1.outputs[16].hide = True
    group_input_003_1.outputs[17].hide = True

    # node Integer
    integer_1 = hole.nodes.new("FunctionNodeInputInt")
    integer_1.name = "Integer"
    integer_1.integer = 3

    # node Reroute.011
    reroute_011 = hole.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.socket_idname = "NodeSocketGeometry"
    # node Math
    math_3 = hole.nodes.new("ShaderNodeMath")
    math_3.name = "Math"
    math_3.operation = "MULTIPLY"
    math_3.use_clamp = False

    # node Transform Geometry.001
    transform_geometry_001 = hole.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = "COMPONENTS"
    transform_geometry_001.inputs[2].hide = True
    transform_geometry_001.inputs[3].hide = True
    # Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Capture Attribute
    capture_attribute = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new("FLOAT", "Value")
    capture_attribute.capture_items["Value"].data_type = "FLOAT_VECTOR"
    capture_attribute.domain = "FACE"

    # node Normal
    normal_1 = hole.nodes.new("GeometryNodeInputNormal")
    normal_1.name = "Normal"

    # node Reroute.012
    reroute_012 = hole.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.socket_idname = "NodeSocketGeometry"
    # node Vector Math.003
    vector_math_003 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = "NORMALIZE"

    # node Vector Math.004
    vector_math_004 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = "SCALE"

    # node Vector Math.005
    vector_math_005 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.operation = "DOT_PRODUCT"

    # node Reroute.013
    reroute_013 = hole.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.socket_idname = "NodeSocketVector"
    # node Normal.001
    normal_001_1 = hole.nodes.new("GeometryNodeInputNormal")
    normal_001_1.name = "Normal.001"

    # node Math.001
    math_001_3 = hole.nodes.new("ShaderNodeMath")
    math_001_3.name = "Math.001"
    math_001_3.operation = "MULTIPLY"
    math_001_3.use_clamp = False
    # Value_001
    math_001_3.inputs[1].default_value = 0.5

    # node Vector Math.006
    vector_math_006 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_006.name = "Vector Math.006"
    vector_math_006.operation = "SUBTRACT"

    # node Group Input.004
    group_input_004_1 = hole.nodes.new("NodeGroupInput")
    group_input_004_1.name = "Group Input.004"
    group_input_004_1.outputs[0].hide = True
    group_input_004_1.outputs[1].hide = True
    group_input_004_1.outputs[2].hide = True
    group_input_004_1.outputs[3].hide = True
    group_input_004_1.outputs[4].hide = True
    group_input_004_1.outputs[5].hide = True
    group_input_004_1.outputs[6].hide = True
    group_input_004_1.outputs[7].hide = True
    group_input_004_1.outputs[8].hide = True
    group_input_004_1.outputs[9].hide = True
    group_input_004_1.outputs[10].hide = True
    group_input_004_1.outputs[11].hide = True
    group_input_004_1.outputs[13].hide = True
    group_input_004_1.outputs[14].hide = True
    group_input_004_1.outputs[15].hide = True
    group_input_004_1.outputs[16].hide = True
    group_input_004_1.outputs[17].hide = True

    # node Vector Math.007
    vector_math_007 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_007.name = "Vector Math.007"
    vector_math_007.operation = "SCALE"

    # node Capture Attribute.001
    capture_attribute_001 = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_001.name = "Capture Attribute.001"
    capture_attribute_001.active_index = 0
    capture_attribute_001.capture_items.clear()
    capture_attribute_001.capture_items.new("FLOAT", "Value")
    capture_attribute_001.capture_items["Value"].data_type = "FLOAT_VECTOR"
    capture_attribute_001.domain = "FACE"

    # node Vector Rotate.001
    vector_rotate_001 = hole.nodes.new("ShaderNodeVectorRotate")
    vector_rotate_001.name = "Vector Rotate.001"
    vector_rotate_001.invert = False
    vector_rotate_001.rotation_type = "EULER_XYZ"

    # node Vector Math.008
    vector_math_008 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_008.name = "Vector Math.008"
    vector_math_008.operation = "ADD"

    # node Vector Math.009
    vector_math_009 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_009.name = "Vector Math.009"
    vector_math_009.operation = "ADD"

    # node Reroute.014
    reroute_014 = hole.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.socket_idname = "NodeSocketVectorEuler"
    # node Group Input.005
    group_input_005_1 = hole.nodes.new("NodeGroupInput")
    group_input_005_1.name = "Group Input.005"
    group_input_005_1.outputs[0].hide = True
    group_input_005_1.outputs[1].hide = True
    group_input_005_1.outputs[2].hide = True
    group_input_005_1.outputs[4].hide = True
    group_input_005_1.outputs[5].hide = True
    group_input_005_1.outputs[6].hide = True
    group_input_005_1.outputs[7].hide = True
    group_input_005_1.outputs[8].hide = True
    group_input_005_1.outputs[9].hide = True
    group_input_005_1.outputs[10].hide = True
    group_input_005_1.outputs[11].hide = True
    group_input_005_1.outputs[12].hide = True
    group_input_005_1.outputs[13].hide = True
    group_input_005_1.outputs[14].hide = True
    group_input_005_1.outputs[15].hide = True
    group_input_005_1.outputs[16].hide = True
    group_input_005_1.outputs[17].hide = True

    # node Object Info.001
    object_info_001 = hole.nodes.new("GeometryNodeObjectInfo")
    object_info_001.name = "Object Info.001"
    object_info_001.transform_space = "RELATIVE"
    object_info_001.inputs[1].hide = True
    object_info_001.outputs[3].hide = True
    object_info_001.outputs[4].hide = True
    # As Instance
    object_info_001.inputs[1].default_value = False

    # node Vector Math.010
    vector_math_010 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_010.name = "Vector Math.010"
    vector_math_010.operation = "MULTIPLY"

    # node Vector Math.011
    vector_math_011 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_011.name = "Vector Math.011"
    vector_math_011.operation = "MULTIPLY"

    # node Combine XYZ
    combine_xyz_2 = hole.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_2.name = "Combine XYZ"
    combine_xyz_2.inputs[0].hide = True
    combine_xyz_2.inputs[2].hide = True
    # X
    combine_xyz_2.inputs[0].default_value = 0.0
    # Z
    combine_xyz_2.inputs[2].default_value = 0.0

    # node Combine XYZ.001
    combine_xyz_001 = hole.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.inputs[1].hide = True
    combine_xyz_001.inputs[2].hide = True
    # Y
    combine_xyz_001.inputs[1].default_value = 0.0
    # Z
    combine_xyz_001.inputs[2].default_value = 0.0

    # node Separate XYZ.001
    separate_xyz_001 = hole.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"

    # node Integer.001
    integer_001_1 = hole.nodes.new("FunctionNodeInputInt")
    integer_001_1.name = "Integer.001"
    integer_001_1.integer = 0

    # node Group Input.006
    group_input_006_1 = hole.nodes.new("NodeGroupInput")
    group_input_006_1.name = "Group Input.006"
    group_input_006_1.outputs[0].hide = True
    group_input_006_1.outputs[1].hide = True
    group_input_006_1.outputs[2].hide = True
    group_input_006_1.outputs[3].hide = True
    group_input_006_1.outputs[6].hide = True
    group_input_006_1.outputs[7].hide = True
    group_input_006_1.outputs[8].hide = True
    group_input_006_1.outputs[9].hide = True
    group_input_006_1.outputs[10].hide = True
    group_input_006_1.outputs[11].hide = True
    group_input_006_1.outputs[12].hide = True
    group_input_006_1.outputs[13].hide = True
    group_input_006_1.outputs[14].hide = True
    group_input_006_1.outputs[15].hide = True
    group_input_006_1.outputs[16].hide = True
    group_input_006_1.outputs[17].hide = True

    # node Group Input.007
    group_input_007_1 = hole.nodes.new("NodeGroupInput")
    group_input_007_1.name = "Group Input.007"
    group_input_007_1.outputs[0].hide = True
    group_input_007_1.outputs[2].hide = True
    group_input_007_1.outputs[3].hide = True
    group_input_007_1.outputs[4].hide = True
    group_input_007_1.outputs[5].hide = True
    group_input_007_1.outputs[6].hide = True
    group_input_007_1.outputs[7].hide = True
    group_input_007_1.outputs[8].hide = True
    group_input_007_1.outputs[9].hide = True
    group_input_007_1.outputs[10].hide = True
    group_input_007_1.outputs[11].hide = True
    group_input_007_1.outputs[12].hide = True
    group_input_007_1.outputs[13].hide = True
    group_input_007_1.outputs[14].hide = True
    group_input_007_1.outputs[15].hide = True
    group_input_007_1.outputs[16].hide = True
    group_input_007_1.outputs[17].hide = True

    # node Random Value.001
    random_value_001_1 = hole.nodes.new("FunctionNodeRandomValue")
    random_value_001_1.name = "Random Value.001"
    random_value_001_1.data_type = "FLOAT_VECTOR"

    # node Group
    group = hole.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = _get_parallel_vectors

    # node Group Input.008
    group_input_008_1 = hole.nodes.new("NodeGroupInput")
    group_input_008_1.name = "Group Input.008"
    group_input_008_1.outputs[0].hide = True
    group_input_008_1.outputs[2].hide = True
    group_input_008_1.outputs[3].hide = True
    group_input_008_1.outputs[4].hide = True
    group_input_008_1.outputs[5].hide = True
    group_input_008_1.outputs[6].hide = True
    group_input_008_1.outputs[7].hide = True
    group_input_008_1.outputs[8].hide = True
    group_input_008_1.outputs[9].hide = True
    group_input_008_1.outputs[10].hide = True
    group_input_008_1.outputs[11].hide = True
    group_input_008_1.outputs[12].hide = True
    group_input_008_1.outputs[13].hide = True
    group_input_008_1.outputs[14].hide = True
    group_input_008_1.outputs[15].hide = True
    group_input_008_1.outputs[16].hide = True
    group_input_008_1.outputs[17].hide = True

    # node Integer.002
    integer_002_1 = hole.nodes.new("FunctionNodeInputInt")
    integer_002_1.name = "Integer.002"
    integer_002_1.integer = 1

    # node Group Input.009
    group_input_009_1 = hole.nodes.new("NodeGroupInput")
    group_input_009_1.name = "Group Input.009"
    group_input_009_1.outputs[0].hide = True
    group_input_009_1.outputs[1].hide = True
    group_input_009_1.outputs[2].hide = True
    group_input_009_1.outputs[3].hide = True
    group_input_009_1.outputs[4].hide = True
    group_input_009_1.outputs[5].hide = True
    group_input_009_1.outputs[8].hide = True
    group_input_009_1.outputs[9].hide = True
    group_input_009_1.outputs[10].hide = True
    group_input_009_1.outputs[11].hide = True
    group_input_009_1.outputs[12].hide = True
    group_input_009_1.outputs[13].hide = True
    group_input_009_1.outputs[14].hide = True
    group_input_009_1.outputs[15].hide = True
    group_input_009_1.outputs[16].hide = True
    group_input_009_1.outputs[17].hide = True

    # node Random Value.002
    random_value_002_1 = hole.nodes.new("FunctionNodeRandomValue")
    random_value_002_1.name = "Random Value.002"
    random_value_002_1.data_type = "FLOAT_VECTOR"

    # node Normal.002
    normal_002 = hole.nodes.new("GeometryNodeInputNormal")
    normal_002.name = "Normal.002"

    # node Group Input.010
    group_input_010_1 = hole.nodes.new("NodeGroupInput")
    group_input_010_1.name = "Group Input.010"
    group_input_010_1.outputs[1].hide = True
    group_input_010_1.outputs[2].hide = True
    group_input_010_1.outputs[3].hide = True
    group_input_010_1.outputs[4].hide = True
    group_input_010_1.outputs[5].hide = True
    group_input_010_1.outputs[6].hide = True
    group_input_010_1.outputs[7].hide = True
    group_input_010_1.outputs[8].hide = True
    group_input_010_1.outputs[9].hide = True
    group_input_010_1.outputs[10].hide = True
    group_input_010_1.outputs[11].hide = True
    group_input_010_1.outputs[12].hide = True
    group_input_010_1.outputs[13].hide = True
    group_input_010_1.outputs[14].hide = True
    group_input_010_1.outputs[15].hide = True
    group_input_010_1.outputs[16].hide = True
    group_input_010_1.outputs[17].hide = True

    # node Sample Nearest Surface
    sample_nearest_surface = hole.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface.name = "Sample Nearest Surface"
    sample_nearest_surface.data_type = "FLOAT_VECTOR"
    # Group ID
    sample_nearest_surface.inputs[2].default_value = 0
    # Sample Group ID
    sample_nearest_surface.inputs[4].default_value = 0

    # node Vector Math.012
    vector_math_012 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_012.name = "Vector Math.012"
    vector_math_012.operation = "ADD"

    # node Reroute.015
    reroute_015 = hole.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.socket_idname = "NodeSocketVector"
    # node Group Input.011
    group_input_011_1 = hole.nodes.new("NodeGroupInput")
    group_input_011_1.name = "Group Input.011"
    group_input_011_1.outputs[0].hide = True
    group_input_011_1.outputs[2].hide = True
    group_input_011_1.outputs[3].hide = True
    group_input_011_1.outputs[4].hide = True
    group_input_011_1.outputs[5].hide = True
    group_input_011_1.outputs[6].hide = True
    group_input_011_1.outputs[7].hide = True
    group_input_011_1.outputs[8].hide = True
    group_input_011_1.outputs[9].hide = True
    group_input_011_1.outputs[10].hide = True
    group_input_011_1.outputs[11].hide = True
    group_input_011_1.outputs[12].hide = True
    group_input_011_1.outputs[13].hide = True
    group_input_011_1.outputs[14].hide = True
    group_input_011_1.outputs[15].hide = True
    group_input_011_1.outputs[16].hide = True
    group_input_011_1.outputs[17].hide = True

    # node Group Input.012
    group_input_012_1 = hole.nodes.new("NodeGroupInput")
    group_input_012_1.name = "Group Input.012"
    group_input_012_1.outputs[0].hide = True
    group_input_012_1.outputs[1].hide = True
    group_input_012_1.outputs[2].hide = True
    group_input_012_1.outputs[3].hide = True
    group_input_012_1.outputs[4].hide = True
    group_input_012_1.outputs[5].hide = True
    group_input_012_1.outputs[6].hide = True
    group_input_012_1.outputs[7].hide = True
    group_input_012_1.outputs[10].hide = True
    group_input_012_1.outputs[11].hide = True
    group_input_012_1.outputs[12].hide = True
    group_input_012_1.outputs[13].hide = True
    group_input_012_1.outputs[14].hide = True
    group_input_012_1.outputs[15].hide = True
    group_input_012_1.outputs[16].hide = True
    group_input_012_1.outputs[17].hide = True

    # node Integer.003
    integer_003_1 = hole.nodes.new("FunctionNodeInputInt")
    integer_003_1.name = "Integer.003"
    integer_003_1.integer = 2

    # node Random Value.003
    random_value_003_1 = hole.nodes.new("FunctionNodeRandomValue")
    random_value_003_1.name = "Random Value.003"
    random_value_003_1.data_type = "FLOAT"

    # node Combine XYZ.002
    combine_xyz_002 = hole.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.inputs[0].hide = True
    combine_xyz_002.inputs[1].hide = True
    # X
    combine_xyz_002.inputs[0].default_value = 0.0
    # Y
    combine_xyz_002.inputs[1].default_value = 0.0

    # node Normal.003
    normal_003 = hole.nodes.new("GeometryNodeInputNormal")
    normal_003.name = "Normal.003"

    # node Capture Attribute.002
    capture_attribute_002 = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_002.name = "Capture Attribute.002"
    capture_attribute_002.active_index = 0
    capture_attribute_002.capture_items.clear()
    capture_attribute_002.capture_items.new("FLOAT", "Value")
    capture_attribute_002.capture_items["Value"].data_type = "FLOAT_VECTOR"
    capture_attribute_002.domain = "FACE"

    # node Transform Geometry.002
    transform_geometry_002 = hole.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = "COMPONENTS"
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    # Rotation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Group Input.013
    group_input_013_1 = hole.nodes.new("NodeGroupInput")
    group_input_013_1.name = "Group Input.013"
    group_input_013_1.outputs[0].hide = True
    group_input_013_1.outputs[1].hide = True
    group_input_013_1.outputs[2].hide = True
    group_input_013_1.outputs[3].hide = True
    group_input_013_1.outputs[4].hide = True
    group_input_013_1.outputs[5].hide = True
    group_input_013_1.outputs[6].hide = True
    group_input_013_1.outputs[7].hide = True
    group_input_013_1.outputs[8].hide = True
    group_input_013_1.outputs[9].hide = True
    group_input_013_1.outputs[10].hide = True
    group_input_013_1.outputs[11].hide = True
    group_input_013_1.outputs[12].hide = True
    group_input_013_1.outputs[13].hide = True
    group_input_013_1.outputs[15].hide = True
    group_input_013_1.outputs[16].hide = True
    group_input_013_1.outputs[17].hide = True

    # node Vector Math.013
    vector_math_013 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_013.name = "Vector Math.013"
    vector_math_013.operation = "SCALE"

    # node Compare
    compare_1 = hole.nodes.new("FunctionNodeCompare")
    compare_1.name = "Compare"
    compare_1.data_type = "VECTOR"
    compare_1.mode = "DIRECTION"
    compare_1.operation = "LESS_THAN"
    # Angle
    compare_1.inputs[11].default_value = 1.5620696544647217

    # node Transform Geometry.003
    transform_geometry_003 = hole.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = "COMPONENTS"
    transform_geometry_003.inputs[3].hide = True
    # Scale
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Reroute.016
    reroute_016 = hole.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.socket_idname = "NodeSocketGeometry"
    # node Vector Math.014
    vector_math_014 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_014.name = "Vector Math.014"
    vector_math_014.operation = "SCALE"

    # node Vector Math.015
    vector_math_015 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_015.name = "Vector Math.015"
    vector_math_015.operation = "NORMALIZE"

    # node Vector Math.016
    vector_math_016 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_016.name = "Vector Math.016"
    vector_math_016.operation = "SUBTRACT"

    # node Vector Math.017
    vector_math_017 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_017.name = "Vector Math.017"
    vector_math_017.operation = "SCALE"

    # node Vector Math.018
    vector_math_018 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_018.name = "Vector Math.018"
    vector_math_018.operation = "DOT_PRODUCT"

    # node Reroute.017
    reroute_017 = hole.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.socket_idname = "NodeSocketVector"
    # node Capture Attribute.003
    capture_attribute_003 = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_003.name = "Capture Attribute.003"
    capture_attribute_003.active_index = 0
    capture_attribute_003.capture_items.clear()
    capture_attribute_003.capture_items.new("FLOAT", "Value")
    capture_attribute_003.capture_items["Value"].data_type = "FLOAT_VECTOR"
    capture_attribute_003.domain = "FACE"

    # node Normal.004
    normal_004 = hole.nodes.new("GeometryNodeInputNormal")
    normal_004.name = "Normal.004"

    # node Math.002
    math_002_2 = hole.nodes.new("ShaderNodeMath")
    math_002_2.name = "Math.002"
    math_002_2.operation = "ADD"
    math_002_2.use_clamp = False

    # node Group Input.014
    group_input_014_1 = hole.nodes.new("NodeGroupInput")
    group_input_014_1.name = "Group Input.014"
    group_input_014_1.outputs[0].hide = True
    group_input_014_1.outputs[1].hide = True
    group_input_014_1.outputs[2].hide = True
    group_input_014_1.outputs[3].hide = True
    group_input_014_1.outputs[4].hide = True
    group_input_014_1.outputs[5].hide = True
    group_input_014_1.outputs[6].hide = True
    group_input_014_1.outputs[7].hide = True
    group_input_014_1.outputs[8].hide = True
    group_input_014_1.outputs[9].hide = True
    group_input_014_1.outputs[10].hide = True
    group_input_014_1.outputs[11].hide = True
    group_input_014_1.outputs[12].hide = True
    group_input_014_1.outputs[13].hide = True
    group_input_014_1.outputs[14].hide = True
    group_input_014_1.outputs[16].hide = True
    group_input_014_1.outputs[17].hide = True

    # node Compare.001
    compare_001_1 = hole.nodes.new("FunctionNodeCompare")
    compare_001_1.name = "Compare.001"
    compare_001_1.data_type = "VECTOR"
    compare_001_1.mode = "DIRECTION"
    compare_001_1.operation = "LESS_THAN"
    # Angle
    compare_001_1.inputs[11].default_value = 3.1328659057617188

    # node Capture Attribute.004
    capture_attribute_004 = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_004.name = "Capture Attribute.004"
    capture_attribute_004.active_index = 0
    capture_attribute_004.capture_items.clear()
    capture_attribute_004.capture_items.new("FLOAT", "Value")
    capture_attribute_004.capture_items["Value"].data_type = "FLOAT_VECTOR"
    capture_attribute_004.domain = "FACE"

    # node Normal.005
    normal_005 = hole.nodes.new("GeometryNodeInputNormal")
    normal_005.name = "Normal.005"

    # node Group Input.015
    group_input_015 = hole.nodes.new("NodeGroupInput")
    group_input_015.name = "Group Input.015"
    group_input_015.outputs[0].hide = True
    group_input_015.outputs[1].hide = True
    group_input_015.outputs[2].hide = True
    group_input_015.outputs[3].hide = True
    group_input_015.outputs[4].hide = True
    group_input_015.outputs[5].hide = True
    group_input_015.outputs[6].hide = True
    group_input_015.outputs[7].hide = True
    group_input_015.outputs[8].hide = True
    group_input_015.outputs[9].hide = True
    group_input_015.outputs[10].hide = True
    group_input_015.outputs[11].hide = True
    group_input_015.outputs[12].hide = True
    group_input_015.outputs[13].hide = True
    group_input_015.outputs[14].hide = True
    group_input_015.outputs[15].hide = True
    group_input_015.outputs[17].hide = True

    # node Capture Attribute.005
    capture_attribute_005 = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_005.name = "Capture Attribute.005"
    capture_attribute_005.active_index = 0
    capture_attribute_005.capture_items.clear()
    capture_attribute_005.capture_items.new("FLOAT", "Value")
    capture_attribute_005.capture_items["Value"].data_type = "FLOAT_VECTOR"
    capture_attribute_005.domain = "FACE"

    # node Normal.006
    normal_006 = hole.nodes.new("GeometryNodeInputNormal")
    normal_006.name = "Normal.006"

    # node Group Input.016
    group_input_016 = hole.nodes.new("NodeGroupInput")
    group_input_016.name = "Group Input.016"
    group_input_016.outputs[1].hide = True
    group_input_016.outputs[2].hide = True
    group_input_016.outputs[3].hide = True
    group_input_016.outputs[4].hide = True
    group_input_016.outputs[5].hide = True
    group_input_016.outputs[6].hide = True
    group_input_016.outputs[7].hide = True
    group_input_016.outputs[8].hide = True
    group_input_016.outputs[9].hide = True
    group_input_016.outputs[10].hide = True
    group_input_016.outputs[11].hide = True
    group_input_016.outputs[12].hide = True
    group_input_016.outputs[13].hide = True
    group_input_016.outputs[14].hide = True
    group_input_016.outputs[15].hide = True
    group_input_016.outputs[16].hide = True
    group_input_016.outputs[17].hide = True

    # node Sample Nearest Surface.001
    sample_nearest_surface_001 = hole.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface_001.name = "Sample Nearest Surface.001"
    sample_nearest_surface_001.data_type = "FLOAT_VECTOR"
    # Group ID
    sample_nearest_surface_001.inputs[2].default_value = 0
    # Sample Group ID
    sample_nearest_surface_001.inputs[4].default_value = 0

    # node Delete Geometry
    delete_geometry_1 = hole.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_1.name = "Delete Geometry"
    delete_geometry_1.domain = "FACE"
    delete_geometry_1.mode = "ALL"

    # node Compare.002
    compare_002_1 = hole.nodes.new("FunctionNodeCompare")
    compare_002_1.name = "Compare.002"
    compare_002_1.data_type = "VECTOR"
    compare_002_1.mode = "DIRECTION"
    compare_002_1.operation = "NOT_EQUAL"
    # Angle
    compare_002_1.inputs[11].default_value = 3.1415927410125732
    # Epsilon
    compare_002_1.inputs[12].default_value = 0.10000000149011612

    # node Mesh Boolean
    mesh_boolean = hole.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = "DIFFERENCE"
    mesh_boolean.solver = "EXACT"
    # Self Intersection
    mesh_boolean.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean.inputs[3].default_value = False

    # node Mesh Boolean.001
    mesh_boolean_001 = hole.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_001.name = "Mesh Boolean.001"
    mesh_boolean_001.operation = "UNION"
    mesh_boolean_001.solver = "EXACT"
    # Self Intersection
    mesh_boolean_001.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean_001.inputs[3].default_value = False

    # node Group Input.017
    group_input_017 = hole.nodes.new("NodeGroupInput")
    group_input_017.name = "Group Input.017"
    group_input_017.outputs[1].hide = True
    group_input_017.outputs[2].hide = True
    group_input_017.outputs[3].hide = True
    group_input_017.outputs[4].hide = True
    group_input_017.outputs[5].hide = True
    group_input_017.outputs[6].hide = True
    group_input_017.outputs[7].hide = True
    group_input_017.outputs[8].hide = True
    group_input_017.outputs[9].hide = True
    group_input_017.outputs[10].hide = True
    group_input_017.outputs[11].hide = True
    group_input_017.outputs[12].hide = True
    group_input_017.outputs[13].hide = True
    group_input_017.outputs[14].hide = True
    group_input_017.outputs[15].hide = True
    group_input_017.outputs[16].hide = True
    group_input_017.outputs[17].hide = True

    # node Transform Geometry.004
    transform_geometry_004 = hole.nodes.new("GeometryNodeTransform")
    transform_geometry_004.name = "Transform Geometry.004"
    transform_geometry_004.mode = "COMPONENTS"
    transform_geometry_004.inputs[1].hide = True
    transform_geometry_004.inputs[3].hide = True
    # Translation
    transform_geometry_004.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Group Input.018
    group_input_018 = hole.nodes.new("NodeGroupInput")
    group_input_018.name = "Group Input.018"
    group_input_018.outputs[0].hide = True
    group_input_018.outputs[1].hide = True
    group_input_018.outputs[3].hide = True
    group_input_018.outputs[4].hide = True
    group_input_018.outputs[5].hide = True
    group_input_018.outputs[6].hide = True
    group_input_018.outputs[7].hide = True
    group_input_018.outputs[8].hide = True
    group_input_018.outputs[9].hide = True
    group_input_018.outputs[10].hide = True
    group_input_018.outputs[11].hide = True
    group_input_018.outputs[12].hide = True
    group_input_018.outputs[13].hide = True
    group_input_018.outputs[14].hide = True
    group_input_018.outputs[15].hide = True
    group_input_018.outputs[16].hide = True
    group_input_018.outputs[17].hide = True

    # node Object Info.002
    object_info_002 = hole.nodes.new("GeometryNodeObjectInfo")
    object_info_002.name = "Object Info.002"
    object_info_002.transform_space = "ORIGINAL"
    object_info_002.inputs[1].hide = True
    object_info_002.outputs[1].hide = True
    object_info_002.outputs[2].hide = True
    object_info_002.outputs[3].hide = True
    # As Instance
    object_info_002.inputs[1].default_value = False

    # node Convex Hull
    convex_hull = hole.nodes.new("GeometryNodeConvexHull")
    convex_hull.name = "Convex Hull"

    # node Compare.003
    compare_003_1 = hole.nodes.new("FunctionNodeCompare")
    compare_003_1.name = "Compare.003"
    compare_003_1.data_type = "VECTOR"
    compare_003_1.mode = "DIRECTION"
    compare_003_1.operation = "LESS_THAN"
    # Angle
    compare_003_1.inputs[11].default_value = 1.5620696544647217

    # node Reroute.018
    reroute_018 = hole.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.socket_idname = "NodeSocketVector"
    # node Attribute Statistic.001
    attribute_statistic_001 = hole.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_001.name = "Attribute Statistic.001"
    attribute_statistic_001.data_type = "FLOAT"
    attribute_statistic_001.domain = "FACE"
    attribute_statistic_001.inputs[1].hide = True
    attribute_statistic_001.outputs[0].hide = True
    attribute_statistic_001.outputs[2].hide = True
    attribute_statistic_001.outputs[3].hide = True
    attribute_statistic_001.outputs[4].hide = True
    attribute_statistic_001.outputs[5].hide = True
    attribute_statistic_001.outputs[6].hide = True
    attribute_statistic_001.outputs[7].hide = True
    # Selection
    attribute_statistic_001.inputs[1].default_value = True

    # node Object Info.003
    object_info_003 = hole.nodes.new("GeometryNodeObjectInfo")
    object_info_003.name = "Object Info.003"
    object_info_003.transform_space = "ORIGINAL"
    object_info_003.inputs[1].hide = True
    object_info_003.outputs[1].hide = True
    object_info_003.outputs[2].hide = True
    object_info_003.outputs[3].hide = True
    # As Instance
    object_info_003.inputs[1].default_value = False

    # node Is Shade Smooth
    is_shade_smooth = hole.nodes.new("GeometryNodeInputShadeSmooth")
    is_shade_smooth.name = "Is Shade Smooth"

    # node Group Input.019
    group_input_019 = hole.nodes.new("NodeGroupInput")
    group_input_019.name = "Group Input.019"
    group_input_019.outputs[0].hide = True
    group_input_019.outputs[1].hide = True
    group_input_019.outputs[3].hide = True
    group_input_019.outputs[4].hide = True
    group_input_019.outputs[5].hide = True
    group_input_019.outputs[6].hide = True
    group_input_019.outputs[7].hide = True
    group_input_019.outputs[8].hide = True
    group_input_019.outputs[9].hide = True
    group_input_019.outputs[10].hide = True
    group_input_019.outputs[11].hide = True
    group_input_019.outputs[12].hide = True
    group_input_019.outputs[13].hide = True
    group_input_019.outputs[14].hide = True
    group_input_019.outputs[15].hide = True
    group_input_019.outputs[16].hide = True
    group_input_019.outputs[17].hide = True

    # node Compare.004
    compare_004_1 = hole.nodes.new("FunctionNodeCompare")
    compare_004_1.name = "Compare.004"
    compare_004_1.data_type = "VECTOR"
    compare_004_1.mode = "DIRECTION"
    compare_004_1.operation = "GREATER_THAN"
    # Angle
    compare_004_1.inputs[11].default_value = 1.579522967338562

    # node Reroute.019
    reroute_019 = hole.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.socket_idname = "NodeSocketVector"
    # node Group Input.020
    group_input_020 = hole.nodes.new("NodeGroupInput")
    group_input_020.name = "Group Input.020"
    group_input_020.outputs[0].hide = True
    group_input_020.outputs[1].hide = True
    group_input_020.outputs[2].hide = True
    group_input_020.outputs[3].hide = True
    group_input_020.outputs[4].hide = True
    group_input_020.outputs[5].hide = True
    group_input_020.outputs[6].hide = True
    group_input_020.outputs[7].hide = True
    group_input_020.outputs[8].hide = True
    group_input_020.outputs[9].hide = True
    group_input_020.outputs[10].hide = True
    group_input_020.outputs[11].hide = True
    group_input_020.outputs[12].hide = True
    group_input_020.outputs[13].hide = True
    group_input_020.outputs[14].hide = True
    group_input_020.outputs[16].hide = True
    group_input_020.outputs[17].hide = True

    # node Vector Math.019
    vector_math_019 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_019.name = "Vector Math.019"
    vector_math_019.operation = "SCALE"

    # node Group.001
    group_001 = hole.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = _decimate_planar

    # node Set Shade Smooth
    set_shade_smooth_1 = hole.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_1.name = "Set Shade Smooth"
    set_shade_smooth_1.domain = "FACE"

    # node Boolean Math
    boolean_math = hole.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = "NOR"

    # node Switch.001
    switch_001_1 = hole.nodes.new("GeometryNodeSwitch")
    switch_001_1.name = "Switch.001"
    switch_001_1.input_type = "GEOMETRY"

    # node Set Position.001
    set_position_001 = hole.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    # Selection
    set_position_001.inputs[1].default_value = True
    # Position
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Set Position.002
    set_position_002 = hole.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    # Position
    set_position_002.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Switch.002
    switch_002_1 = hole.nodes.new("GeometryNodeSwitch")
    switch_002_1.name = "Switch.002"
    switch_002_1.input_type = "GEOMETRY"

    # node Reroute.020
    reroute_020 = hole.nodes.new("NodeReroute")
    reroute_020.label = "peg_insert_direction"
    reroute_020.name = "Reroute.020"
    reroute_020.socket_idname = "NodeSocketVector"
    # node Vector Math.020
    vector_math_020 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_020.name = "Vector Math.020"
    vector_math_020.operation = "SCALE"

    # node Group Input.021
    group_input_021 = hole.nodes.new("NodeGroupInput")
    group_input_021.name = "Group Input.021"
    group_input_021.outputs[1].hide = True
    group_input_021.outputs[2].hide = True
    group_input_021.outputs[3].hide = True
    group_input_021.outputs[4].hide = True
    group_input_021.outputs[5].hide = True
    group_input_021.outputs[6].hide = True
    group_input_021.outputs[7].hide = True
    group_input_021.outputs[8].hide = True
    group_input_021.outputs[9].hide = True
    group_input_021.outputs[10].hide = True
    group_input_021.outputs[11].hide = True
    group_input_021.outputs[12].hide = True
    group_input_021.outputs[13].hide = True
    group_input_021.outputs[14].hide = True
    group_input_021.outputs[15].hide = True
    group_input_021.outputs[16].hide = True
    group_input_021.outputs[17].hide = True

    # node Position.001
    position_001_1 = hole.nodes.new("GeometryNodeInputPosition")
    position_001_1.name = "Position.001"

    # node Sample Nearest Surface.002
    sample_nearest_surface_002 = hole.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface_002.name = "Sample Nearest Surface.002"
    sample_nearest_surface_002.data_type = "FLOAT_VECTOR"
    # Group ID
    sample_nearest_surface_002.inputs[2].default_value = 0
    # Sample Group ID
    sample_nearest_surface_002.inputs[4].default_value = 0

    # node Reroute.021
    reroute_021 = hole.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    reroute_021.socket_idname = "NodeSocketVector"
    # node Vector Math.021
    vector_math_021 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_021.name = "Vector Math.021"
    vector_math_021.operation = "SCALE"
    # Scale
    vector_math_021.inputs[3].default_value = -1.0

    # node Reroute.022
    reroute_022 = hole.nodes.new("NodeReroute")
    reroute_022.label = "hole_position"
    reroute_022.name = "Reroute.022"
    reroute_022.socket_idname = "NodeSocketVector"
    # node Reroute.023
    reroute_023 = hole.nodes.new("NodeReroute")
    reroute_023.label = "peg_pull_direction"
    reroute_023.name = "Reroute.023"
    reroute_023.socket_idname = "NodeSocketVector"
    # node Reroute.024
    reroute_024 = hole.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    reroute_024.socket_idname = "NodeSocketVector"
    # node Vector Math.002
    vector_math_002 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = "SCALE"

    # node Reroute.005
    reroute_005_2 = hole.nodes.new("NodeReroute")
    reroute_005_2.label = "peg_insert_direction"
    reroute_005_2.name = "Reroute.005"
    reroute_005_2.socket_idname = "NodeSocketVector"
    # node Reroute.026
    reroute_026 = hole.nodes.new("NodeReroute")
    reroute_026.name = "Reroute.026"
    reroute_026.socket_idname = "NodeSocketVector"
    # node Reroute.004
    reroute_004_2 = hole.nodes.new("NodeReroute")
    reroute_004_2.label = "peg_with_tolerance"
    reroute_004_2.name = "Reroute.004"
    reroute_004_2.socket_idname = "NodeSocketGeometry"
    # node Switch
    switch_1 = hole.nodes.new("GeometryNodeSwitch")
    switch_1.name = "Switch"
    switch_1.input_type = "GEOMETRY"

    # node Group Input
    group_input_3 = hole.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"
    group_input_3.outputs[1].hide = True
    group_input_3.outputs[2].hide = True
    group_input_3.outputs[3].hide = True
    group_input_3.outputs[4].hide = True
    group_input_3.outputs[5].hide = True
    group_input_3.outputs[6].hide = True
    group_input_3.outputs[7].hide = True
    group_input_3.outputs[8].hide = True
    group_input_3.outputs[9].hide = True
    group_input_3.outputs[10].hide = True
    group_input_3.outputs[11].hide = True
    group_input_3.outputs[12].hide = True
    group_input_3.outputs[14].hide = True
    group_input_3.outputs[15].hide = True
    group_input_3.outputs[16].hide = True
    group_input_3.outputs[17].hide = True

    # node Mesh Boolean.002
    mesh_boolean_002 = hole.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_002.name = "Mesh Boolean.002"
    mesh_boolean_002.operation = "DIFFERENCE"
    mesh_boolean_002.solver = "EXACT"
    # Self Intersection
    mesh_boolean_002.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean_002.inputs[3].default_value = False

    # node Reroute.025
    reroute_025 = hole.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    reroute_025.socket_idname = "NodeSocketVector"
    # node Reroute.028
    reroute_028 = hole.nodes.new("NodeReroute")
    reroute_028.name = "Reroute.028"
    reroute_028.hide = True
    reroute_028.socket_idname = "NodeSocketVector"
    # node Group Output
    group_output_3 = hole.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True

    # node Raycast.001
    raycast_001 = hole.nodes.new("GeometryNodeRaycast")
    raycast_001.name = "Raycast.001"
    raycast_001.data_type = "FLOAT"
    raycast_001.mapping = "INTERPOLATED"
    # Attribute
    raycast_001.inputs[1].default_value = 0.0
    # Ray Length
    raycast_001.inputs[4].default_value = 100.0

    # node Align Euler to Vector.001
    align_euler_to_vector_001 = hole.nodes.new("FunctionNodeAlignEulerToVector")
    align_euler_to_vector_001.name = "Align Euler to Vector.001"
    align_euler_to_vector_001.axis = "Z"
    align_euler_to_vector_001.pivot_axis = "AUTO"
    # Factor
    align_euler_to_vector_001.inputs[1].default_value = 1.0

    # node Vector Math.022
    vector_math_022 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_022.name = "Vector Math.022"
    vector_math_022.operation = "ADD"

    # node Vector Math.023
    vector_math_023 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_023.name = "Vector Math.023"
    vector_math_023.operation = "SCALE"
    # Scale
    vector_math_023.inputs[3].default_value = -1.0

    # node Group Input.022
    group_input_022 = hole.nodes.new("NodeGroupInput")
    group_input_022.name = "Group Input.022"
    group_input_022.outputs[1].hide = True
    group_input_022.outputs[2].hide = True
    group_input_022.outputs[3].hide = True
    group_input_022.outputs[4].hide = True
    group_input_022.outputs[5].hide = True
    group_input_022.outputs[6].hide = True
    group_input_022.outputs[7].hide = True
    group_input_022.outputs[8].hide = True
    group_input_022.outputs[9].hide = True
    group_input_022.outputs[10].hide = True
    group_input_022.outputs[11].hide = True
    group_input_022.outputs[12].hide = True
    group_input_022.outputs[13].hide = True
    group_input_022.outputs[14].hide = True
    group_input_022.outputs[15].hide = True
    group_input_022.outputs[16].hide = True
    group_input_022.outputs[17].hide = True

    # node Raycast
    raycast = hole.nodes.new("GeometryNodeRaycast")
    raycast.name = "Raycast"
    raycast.data_type = "FLOAT"
    raycast.mapping = "INTERPOLATED"
    # Attribute
    raycast.inputs[1].default_value = 0.0
    # Ray Length
    raycast.inputs[4].default_value = 100.0

    # node Extrude Mesh
    extrude_mesh = hole.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.mode = "FACES"
    # Offset Scale
    extrude_mesh.inputs[3].default_value = 1.0
    # Individual
    extrude_mesh.inputs[4].default_value = False

    # node Set Position
    set_position_1 = hole.nodes.new("GeometryNodeSetPosition")
    set_position_1.name = "Set Position"
    # Selection
    set_position_1.inputs[1].default_value = True
    # Position
    set_position_1.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Set Position.003
    set_position_003 = hole.nodes.new("GeometryNodeSetPosition")
    set_position_003.name = "Set Position.003"
    # Position
    set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Rotation to Euler
    rotation_to_euler = hole.nodes.new("FunctionNodeRotationToEuler")
    rotation_to_euler.name = "Rotation to Euler"

    # node Euler to Rotation
    euler_to_rotation = hole.nodes.new("FunctionNodeEulerToRotation")
    euler_to_rotation.name = "Euler to Rotation"

    # node Group.002
    group_002 = hole.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = peg
    # Socket_2
    group_002.inputs[1].default_value = 0.3333333432674408
    # Socket_3
    group_002.inputs[2].default_value = 48
    # Socket_4
    group_002.inputs[3].default_value = 3
    # Socket_5
    group_002.inputs[4].default_value = 12
    # Socket_6
    group_002.inputs[5].default_value = 0.009999999776482582
    # Socket_7
    group_002.inputs[6].default_value = 0.02500000037252903
    # Socket_8
    group_002.inputs[7].default_value = 0.03999999910593033
    # Socket_9
    group_002.inputs[8].default_value = 0.07999999821186066
    # Socket_10
    group_002.inputs[9].default_value = 0.25
    # Socket_11
    group_002.inputs[10].default_value = 1.0
    # Socket_12
    group_002.inputs[11].default_value = 0.0
    # Socket_13
    group_002.inputs[12].default_value = 0.0
    # Socket_14
    group_002.inputs[13].default_value = False

    # node Group Input.024
    group_input_024 = hole.nodes.new("NodeGroupInput")
    group_input_024.name = "Group Input.024"

    # node Vector Math.024
    vector_math_024 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_024.name = "Vector Math.024"
    vector_math_024.operation = "SCALE"
    # Scale
    vector_math_024.inputs[3].default_value = -1.0

    # node Set Material
    set_material_1 = hole.nodes.new("GeometryNodeSetMaterial")
    set_material_1.name = "Set Material"
    # Selection
    set_material_1.inputs[1].default_value = True
    if "Metal" in bpy.data.materials:
        set_material_1.inputs[2].default_value = bpy.data.materials["Metal"]

    # Set parents
    frame_003_2.parent = frame_002_2
    frame_004_2.parent = frame_002_2
    frame_005_2.parent = frame_002_2
    frame_006_2.parent = frame_002_2
    frame_009.parent = frame_001_2
    frame_010.parent = frame_009
    frame_011.parent = frame_001_2
    frame_012.parent = frame_001_2
    frame_013.parent = frame_001_2
    frame_014.parent = frame_001_2
    group_input_001_1.parent = frame_003_2
    position_1.parent = frame_003_2
    object_info.parent = frame_003_2
    attribute_statistic.parent = frame_003_2
    vector_math_2.parent = frame_003_2
    align_euler_to_vector.parent = frame_003_2
    reroute_009.parent = frame_003_2
    separate_xyz_1.parent = frame_003_2
    vector_rotate.parent = frame_003_2
    vector_math_001_2.parent = frame_003_2
    reroute_010.parent = frame_003_2
    transform_geometry_1.parent = frame_003_2
    group_input_002_1.parent = frame_004_2
    random_value_1.parent = frame_004_2
    group_input_003_1.parent = frame_004_2
    integer_1.parent = frame_004_2
    reroute_011.parent = frame_004_2
    math_3.parent = frame_004_2
    transform_geometry_001.parent = frame_004_2
    capture_attribute.parent = frame_005_2
    normal_1.parent = frame_005_2
    reroute_012.parent = frame_006_2
    vector_math_003.parent = frame_006_2
    vector_math_004.parent = frame_006_2
    vector_math_005.parent = frame_006_2
    reroute_013.parent = frame_006_2
    normal_001_1.parent = frame_006_2
    math_001_3.parent = frame_006_2
    vector_math_006.parent = frame_006_2
    group_input_004_1.parent = frame_006_2
    vector_math_007.parent = frame_006_2
    capture_attribute_001.parent = frame_006_2
    vector_rotate_001.parent = frame_007_1
    vector_math_008.parent = frame_007_1
    vector_math_009.parent = frame_007_1
    reroute_014.parent = frame_007_1
    group_input_005_1.parent = frame_007_1
    object_info_001.parent = frame_007_1
    vector_math_010.parent = frame_007_1
    vector_math_011.parent = frame_007_1
    combine_xyz_2.parent = frame_007_1
    combine_xyz_001.parent = frame_007_1
    separate_xyz_001.parent = frame_007_1
    integer_001_1.parent = frame_007_1
    group_input_006_1.parent = frame_007_1
    group_input_007_1.parent = frame_007_1
    random_value_001_1.parent = frame_007_1
    group.parent = frame_007_1
    group_input_008_1.parent = frame_007_1
    integer_002_1.parent = frame_007_1
    group_input_009_1.parent = frame_007_1
    random_value_002_1.parent = frame_007_1
    normal_002.parent = frame_007_1
    group_input_010_1.parent = frame_007_1
    sample_nearest_surface.parent = frame_007_1
    vector_math_012.parent = frame_007_1
    reroute_015.parent = frame_007_1
    group_input_011_1.parent = frame_008_1
    group_input_012_1.parent = frame_008_1
    integer_003_1.parent = frame_008_1
    random_value_003_1.parent = frame_008_1
    combine_xyz_002.parent = frame_008_1
    normal_003.parent = frame_009
    capture_attribute_002.parent = frame_009
    transform_geometry_002.parent = frame_009
    group_input_013_1.parent = frame_009
    vector_math_013.parent = frame_009
    compare_1.parent = frame_009
    transform_geometry_003.parent = frame_009
    reroute_016.parent = frame_011
    vector_math_014.parent = frame_011
    vector_math_015.parent = frame_011
    vector_math_016.parent = frame_011
    vector_math_017.parent = frame_011
    vector_math_018.parent = frame_011
    reroute_017.parent = frame_011
    capture_attribute_003.parent = frame_011
    normal_004.parent = frame_011
    math_002_2.parent = frame_011
    group_input_014_1.parent = frame_011
    compare_001_1.parent = frame_012
    capture_attribute_004.parent = frame_012
    normal_005.parent = frame_012
    group_input_015.parent = frame_012
    capture_attribute_005.parent = frame_013
    normal_006.parent = frame_013
    group_input_016.parent = frame_013
    sample_nearest_surface_001.parent = frame_013
    delete_geometry_1.parent = frame_013
    compare_002_1.parent = frame_013
    mesh_boolean.parent = frame_013
    mesh_boolean_001.parent = frame_014
    group_input_017.parent = frame_014
    transform_geometry_004.parent = frame_008_1
    group_input_018.parent = frame_008_1
    object_info_002.parent = frame_008_1
    convex_hull.parent = frame_010
    compare_003_1.parent = frame_005_2
    reroute_018.parent = frame_005_2
    attribute_statistic_001.parent = frame_005_2
    object_info_003.parent = frame_005_2
    is_shade_smooth.parent = frame_005_2
    group_input_019.parent = frame_005_2
    compare_004_1.parent = frame_005_2
    reroute_019.parent = frame_012
    group_input_020.parent = frame_012
    vector_math_019.parent = frame_012
    group_001.parent = frame_008_1
    set_shade_smooth_1.parent = frame_005_2
    boolean_math.parent = frame_005_2
    switch_001_1.parent = frame_009
    set_position_001.parent = frame_011
    set_position_002.parent = frame_012
    switch_002_1.parent = frame_012
    reroute_020.parent = frame_007_1
    vector_math_020.parent = frame_005_2
    group_input_021.parent = frame_007_1
    position_001_1.parent = frame_007_1
    sample_nearest_surface_002.parent = frame_007_1
    reroute_021.parent = frame_007_1
    vector_math_021.parent = frame_007_1
    reroute_022.parent = frame_007_1
    reroute_023.parent = frame_007_1
    vector_math_002.parent = frame_004_2
    reroute_004_2.parent = frame_2
    switch_1.parent = frame_2
    group_input_3.parent = frame_2
    mesh_boolean_002.parent = frame_2
    extrude_mesh.parent = frame_009
    set_position_1.parent = frame_006_2
    set_position_003.parent = frame_005_2
    rotation_to_euler.parent = frame_007_1
    euler_to_rotation.parent = frame_008_1
    group_002.parent = frame_002_2
    group_input_024.parent = frame_002_2
    vector_math_024.parent = frame_012

    # Set locations
    frame_001_2.location = (513.515625, 190.8028564453125)
    frame_002_2.location = (-4053.509765625, 844.9335327148438)
    frame_003_2.location = (-3648.28271484375, 198.9276123046875)
    frame_004_2.location = (-3128.17529296875, -757.0723876953125)
    frame_005_2.location = (-1750.1142578125, -651.0723876953125)
    frame_006_2.location = (1143.4736328125, -623.0723876953125)
    frame_007_1.location = (-9566.5546875, 252.6092529296875)
    frame_008_1.location = (-9641.5322265625, -783.0304565429688)
    frame_009.location = (-4700.29052734375, -8.06781005859375)
    frame_010.location = (-4567.50390625, -416.68975830078125)
    frame_011.location = (-4291.4853515625, 237.93218994140625)
    frame_012.location = (-2751.08984375, -868.0678100585938)
    frame_013.location = (-690.520263671875, -839.0678100585938)
    frame_014.location = (-978.5537109375, -491.06781005859375)
    frame_2.location = (147.494140625, 473.3194885253906)
    reroute_2.location = (-9989.935546875, -888.8091430664062)
    reroute_001_2.location = (-9663.9150390625, -809.8853149414062)
    reroute_002_2.location = (-9130.2607421875, -1005.8109741210938)
    reroute_003_2.location = (-2314.447265625, -1005.8109741210938)
    reroute_006_2.location = (-5898.68798828125, -942.5845336914062)
    reroute_007_2.location = (-7860.53466796875, -935.8130493164062)
    reroute_008_1.location = (-7538.65966796875, -888.8091430664062)
    group_input_001_1.location = (-2705.15478515625, -624.2618408203125)
    position_1.location = (-2546.97998046875, -729.026123046875)
    object_info.location = (-2509.43701171875, -583.0252685546875)
    attribute_statistic.location = (-2314.43701171875, -559.5252685546875)
    vector_math_2.location = (-2124.43701171875, -583.5276489257812)
    align_euler_to_vector.location = (-2124.43701171875, -825.7966918945312)
    reroute_009.location = (-2133.73974609375, -989.1820678710938)
    separate_xyz_1.location = (-1273.95556640625, -920.3519897460938)
    vector_rotate.location = (-1762.41796875, -616.0169677734375)
    vector_math_001_2.location = (-1472.26806640625, -626.5169677734375)
    reroute_010.location = (-710.29150390625, -959.3439331054688)
    transform_geometry_1.location = (-892.54248046875, -627.1513061523438)
    group_input_002_1.location = (-1077.099609375, 123.12406921386719)
    random_value_1.location = (-887.099609375, 298.0420837402344)
    group_input_003_1.location = (-1077.099609375, 307.12408447265625)
    integer_1.location = (-1077.099609375, 218.12408447265625)
    reroute_011.location = (-1047.9033203125, 345.3209533691406)
    math_3.location = (-697.099609375, 257.94915771484375)
    transform_geometry_001.location = (-317.099609375, 397.04498291015625)
    capture_attribute.location = (-1239.36474609375, 291.3905029296875)
    normal_1.location = (-1429.36474609375, 147.94754028320312)
    reroute_012.location = (-1523.92626953125, 212.9775390625)
    vector_math_003.location = (-1802.8603515625, 73.8314208984375)
    vector_math_004.location = (-1610.84423828125, 55.22772216796875)
    vector_math_005.location = (-2372.8603515625, 83.8314208984375)
    reroute_013.location = (-2747.20068359375, -112.7867431640625)
    normal_001_1.location = (-2750.84423828125, 101.25079345703125)
    math_001_3.location = (-1992.8603515625, -66.50848388671875)
    vector_math_006.location = (-1992.8603515625, 139.49151611328125)
    group_input_004_1.location = (-2182.8603515625, -153.15740966796875)
    vector_math_007.location = (-2182.8603515625, -9.15740966796875)
    capture_attribute_001.location = (-2560.84423828125, 262.5916748046875)
    vector_rotate_001.location = (-2391.31640625, -982.4521484375)
    vector_math_008.location = (-2678.8779296875, -1396.738037109375)
    vector_math_009.location = (-2911.892578125, -1043.40966796875)
    reroute_014.location = (-4063.1611328125, -1506.114501953125)
    group_input_005_1.location = (-4556.3837890625, -904.8895874023438)
    object_info_001.location = (-4366.3837890625, -876.3895874023438)
    vector_math_010.location = (-3101.892578125, -1043.40966796875)
    vector_math_011.location = (-3101.892578125, -1189.40966796875)
    combine_xyz_2.location = (-3451.7255859375, -1233.3857421875)
    combine_xyz_001.location = (-3451.7255859375, -1141.3857421875)
    separate_xyz_001.location = (-3641.7255859375, -1236.4434814453125)
    integer_001_1.location = (-4021.7255859375, -1278.84033203125)
    group_input_006_1.location = (-4021.7255859375, -1189.84033203125)
    group_input_007_1.location = (-4021.7255859375, -1373.84033203125)
    random_value_001_1.location = (-3831.7255859375, -1209.4434814453125)
    group.location = (-3451.7255859375, -938.2553100585938)
    group_input_008_1.location = (-4021.7255859375, -1714.110595703125)
    integer_002_1.location = (-4021.7255859375, -1619.110595703125)
    group_input_009_1.location = (-4021.7255859375, -1530.110595703125)
    random_value_002_1.location = (-3831.7255859375, -1552.233154296875)
    normal_002.location = (-4079.3896484375, -673.62548828125)
    group_input_010_1.location = (-4079.3896484375, -606.62548828125)
    sample_nearest_surface.location = (-3889.3896484375, -616.0238037109375)
    vector_math_012.location = (-2682.44921875, -790.1663818359375)
    reroute_015.location = (-2549.3232421875, -653.9478149414062)
    group_input_011_1.location = (-1077.099609375, 123.12406921386719)
    group_input_012_1.location = (-1077.099609375, 307.12408447265625)
    integer_003_1.location = (-1077.099609375, 218.12408447265625)
    random_value_003_1.location = (-887.099609375, 298.0420837402344)
    combine_xyz_002.location = (-697.099609375, 298.1568603515625)
    normal_003.location = (-3044.212890625, -527.2911376953125)
    capture_attribute_002.location = (-2854.212890625, -383.84814453125)
    transform_geometry_002.location = (-3310.3095703125, -420.71014404296875)
    group_input_013_1.location = (-1936.98779296875, -388.0589294433594)
    vector_math_013.location = (-2664.212890625, -698.5078735351562)
    compare_1.location = (-2664.212890625, -482.50787353515625)
    transform_geometry_003.location = (-4407.046875, -422.1256103515625)
    reroute_016.location = (-654.991943359375, -655.7918701171875)
    vector_math_014.location = (-758.6435546875, -793.4281005859375)
    vector_math_015.location = (-931.909912109375, -803.4281005859375)
    vector_math_016.location = (-1121.909912109375, -792.4281005859375)
    vector_math_017.location = (-1311.91015625, -886.4169311523438)
    vector_math_018.location = (-1501.909912109375, -793.4281005859375)
    reroute_017.location = (-1557.5458984375, -977.3161010742188)
    capture_attribute_003.location = (-1691.909912109375, -614.361572265625)
    normal_004.location = (-1881.91015625, -775.7024536132812)
    math_002_2.location = (-931.91015625, -939.255126953125)
    group_input_014_1.location = (-1121.91015625, -990.2550659179688)
    compare_001_1.location = (-1347.625, 142.58035278320312)
    capture_attribute_004.location = (-1613.553955078125, 249.26657104492188)
    normal_005.location = (-1803.553955078125, 99.11129760742188)
    group_input_015.location = (-477.7353515625, 440.43438720703125)
    capture_attribute_005.location = (-1847.3251953125, 209.8366241455078)
    normal_006.location = (-2042.3253173828125, -24.706893920898438)
    group_input_016.location = (-2042.3253173828125, 42.29313659667969)
    sample_nearest_surface_001.location = (-1852.3251953125, -20.496978759765625)
    delete_geometry_1.location = (-1462.3251953125, 290.1592712402344)
    compare_002_1.location = (-1652.3251953125, 107.35844421386719)
    mesh_boolean.location = (-1191.428466796875, 463.03387451171875)
    mesh_boolean_001.location = (-408.521240234375, 77.7578125)
    group_input_017.location = (-643.92822265625, 114.47882080078125)
    transform_geometry_004.location = (-317.099609375, 388.1473693847656)
    group_input_018.location = (-887.099609375, 378.1298828125)
    object_info_002.location = (-697.099609375, 431.916748046875)
    convex_hull.location = (-217.3515625, -140.37908935546875)
    compare_003_1.location = (-1049.36474609375, 192.73077392578125)
    reroute_018.location = (-1089.38330078125, 17.827835083007812)
    attribute_statistic_001.location = (-513.826171875, 27.43878173828125)
    object_info_003.location = (-705.20654296875, 31.53857421875)
    is_shade_smooth.location = (-705.20654296875, -90.46142578125)
    group_input_019.location = (-873.6982421875, -72.11468505859375)
    compare_004_1.location = (-1048.46484375, 459.92205810546875)
    reroute_019.location = (-1457.640625, -127.03033447265625)
    group_input_020.location = (-1309.314697265625, -110.83929443359375)
    vector_math_019.location = (-1065.810302734375, 57.53192138671875)
    group_001.location = (-507.099609375, 420.97442626953125)
    set_shade_smooth_1.location = (-303.943359375, 283.190185546875)
    boolean_math.location = (-696.56982421875, 448.9088134765625)
    switch_001_1.location = (-1746.98779296875, -368.21966552734375)
    set_position_001.location = (-551.909912109375, -787.4281005859375)
    set_position_002.location = (-705.6748046875, 256.76806640625)
    switch_002_1.location = (-242.73529052734375, 491.57537841796875)
    reroute_020.location = (-1459.109375, -1188.42236328125)
    vector_math_020.location = (-1049.36474609375, -23.26922607421875)
    group_input_021.location = (-2046.375, -691.9337768554688)
    position_001_1.location = (-2046.375, -758.9338989257812)
    sample_nearest_surface_002.location = (-1853.875, -691.8521118164062)
    reroute_021.location = (-1932.453125, -1184.6629638671875)
    vector_math_021.location = (-1847.69140625, -1019.9051513671875)
    reroute_022.location = (-1459.109375, -1062.797119140625)
    reroute_023.location = (-1459.109375, -1141.41845703125)
    reroute_024.location = (-6506.2216796875, 1045.2396240234375)
    vector_math_002.location = (-507.099609375, 245.44915771484375)
    reroute_005_2.location = (-4217.4482421875, -957.7169799804688)
    reroute_026.location = (-599.883056640625, -1244.21435546875)
    reroute_004_2.location = (-609.2918701171875, -223.4200439453125)
    switch_1.location = (-462.2154541015625, -585.3873291015625)
    group_input_3.location = (-652.2154541015625, -624.8873291015625)
    mesh_boolean_002.location = (-87.98570251464844, -316.8748779296875)
    reroute_025.location = (37.5357666015625, 1073.1732177734375)
    reroute_028.location = (-512.5114135742188, -1055.477294921875)
    group_output_3.location = (2515.40380859375, -74.08328247070312)
    raycast_001.location = (864.0977172851562, 492.8777770996094)
    align_euler_to_vector_001.location = (1092.785400390625, 194.20965576171875)
    vector_math_022.location = (795.4451904296875, -892.4864501953125)
    vector_math_023.location = (795.4451904296875, -739.8052368164062)
    group_input_022.location = (795.4451904296875, -656.651123046875)
    raycast.location = (1094.5030517578125, -500.71923828125)
    extrude_mesh.location = (-2232.50830078125, -384.2890625)
    set_position_1.location = (-1420.84423828125, 61.22772216796875)
    set_position_003.location = (-692.2578125, 253.62841796875)
    rotation_to_euler.location = (-4162.873046875, -964.4930419921875)
    euler_to_rotation.location = (-477.724609375, 309.4501647949219)
    group_002.location = (-6626.4619140625, -9.70977783203125)
    group_input_024.location = (-6835.1376953125, -3.41729736328125)
    vector_math_024.location = (-885.42578125, 103.37994384765625)
    set_material_1.location = (1701.5062255859375, -60.55561447143555)

    # Set dimensions
    frame_001_2.width, frame_001_2.height = 8388.0, 833.0
    frame_002_2.width, frame_002_2.height = 6788.0, 935.0
    frame_003_2.width, frame_003_2.height = 2062.916015625, 507.32098388671875
    frame_004_2.width, frame_004_2.height = 960.0, 396.0
    frame_005_2.width, frame_005_2.height = 1325.0, 676.0
    frame_006_2.width, frame_006_2.height = 1534.23681640625, 547.0
    frame_007_1.width, frame_007_1.height = 3165.3359375, 1230.0
    frame_008_1.width, frame_008_1.height = 960.0, 431.0
    frame_009.width, frame_009.height = 3268.0, 524.0
    frame_010.width, frame_010.height = 200.0, 145.0
    frame_011.width, frame_011.height = 1530.0, 543.0000610351562
    frame_012.width, frame_012.height = 1761.0, 724.0
    frame_013.width, frame_013.height = 1051.0, 763.0
    frame_014.width, frame_014.height = 435.0, 297.0
    frame_2.width, frame_2.height = 765.0, 582.8994140625
    reroute_2.width, reroute_2.height = 16.0, 100.0
    reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
    reroute_002_2.width, reroute_002_2.height = 16.0, 100.0
    reroute_003_2.width, reroute_003_2.height = 16.0, 100.0
    reroute_006_2.width, reroute_006_2.height = 16.0, 100.0
    reroute_007_2.width, reroute_007_2.height = 16.0, 100.0
    reroute_008_1.width, reroute_008_1.height = 16.0, 100.0
    group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
    position_1.width, position_1.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
    vector_math_2.width, vector_math_2.height = 140.0, 100.0
    align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
    reroute_009.width, reroute_009.height = 16.0, 100.0
    separate_xyz_1.width, separate_xyz_1.height = 140.0, 100.0
    vector_rotate.width, vector_rotate.height = 140.0, 100.0
    vector_math_001_2.width, vector_math_001_2.height = 140.0, 100.0
    reroute_010.width, reroute_010.height = 16.0, 100.0
    transform_geometry_1.width, transform_geometry_1.height = 140.0, 100.0
    group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
    random_value_1.width, random_value_1.height = 140.0, 100.0
    group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
    integer_1.width, integer_1.height = 140.0, 100.0
    reroute_011.width, reroute_011.height = 16.0, 100.0
    math_3.width, math_3.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    capture_attribute.width, capture_attribute.height = 140.0, 100.0
    normal_1.width, normal_1.height = 140.0, 100.0
    reroute_012.width, reroute_012.height = 16.0, 100.0
    vector_math_003.width, vector_math_003.height = 140.0, 100.0
    vector_math_004.width, vector_math_004.height = 140.0, 100.0
    vector_math_005.width, vector_math_005.height = 140.0, 100.0
    reroute_013.width, reroute_013.height = 16.0, 100.0
    normal_001_1.width, normal_001_1.height = 140.0, 100.0
    math_001_3.width, math_001_3.height = 140.0, 100.0
    vector_math_006.width, vector_math_006.height = 140.0, 100.0
    group_input_004_1.width, group_input_004_1.height = 140.0, 100.0
    vector_math_007.width, vector_math_007.height = 140.0, 100.0
    capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
    vector_rotate_001.width, vector_rotate_001.height = 140.0, 100.0
    vector_math_008.width, vector_math_008.height = 140.0, 100.0
    vector_math_009.width, vector_math_009.height = 140.0, 100.0
    reroute_014.width, reroute_014.height = 16.0, 100.0
    group_input_005_1.width, group_input_005_1.height = 140.0, 100.0
    object_info_001.width, object_info_001.height = 140.0, 100.0
    vector_math_010.width, vector_math_010.height = 140.0, 100.0
    vector_math_011.width, vector_math_011.height = 140.0, 100.0
    combine_xyz_2.width, combine_xyz_2.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    integer_001_1.width, integer_001_1.height = 140.0, 100.0
    group_input_006_1.width, group_input_006_1.height = 140.0, 100.0
    group_input_007_1.width, group_input_007_1.height = 140.0, 100.0
    random_value_001_1.width, random_value_001_1.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0
    group_input_008_1.width, group_input_008_1.height = 140.0, 100.0
    integer_002_1.width, integer_002_1.height = 140.0, 100.0
    group_input_009_1.width, group_input_009_1.height = 140.0, 100.0
    random_value_002_1.width, random_value_002_1.height = 140.0, 100.0
    normal_002.width, normal_002.height = 140.0, 100.0
    group_input_010_1.width, group_input_010_1.height = 140.0, 100.0
    sample_nearest_surface.width, sample_nearest_surface.height = 150.0, 100.0
    vector_math_012.width, vector_math_012.height = 140.0, 100.0
    reroute_015.width, reroute_015.height = 16.0, 100.0
    group_input_011_1.width, group_input_011_1.height = 140.0, 100.0
    group_input_012_1.width, group_input_012_1.height = 140.0, 100.0
    integer_003_1.width, integer_003_1.height = 140.0, 100.0
    random_value_003_1.width, random_value_003_1.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    normal_003.width, normal_003.height = 140.0, 100.0
    capture_attribute_002.width, capture_attribute_002.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    group_input_013_1.width, group_input_013_1.height = 140.0, 100.0
    vector_math_013.width, vector_math_013.height = 140.0, 100.0
    compare_1.width, compare_1.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    reroute_016.width, reroute_016.height = 16.0, 100.0
    vector_math_014.width, vector_math_014.height = 140.0, 100.0
    vector_math_015.width, vector_math_015.height = 140.0, 100.0
    vector_math_016.width, vector_math_016.height = 140.0, 100.0
    vector_math_017.width, vector_math_017.height = 140.0, 100.0
    vector_math_018.width, vector_math_018.height = 140.0, 100.0
    reroute_017.width, reroute_017.height = 16.0, 100.0
    capture_attribute_003.width, capture_attribute_003.height = 140.0, 100.0
    normal_004.width, normal_004.height = 140.0, 100.0
    math_002_2.width, math_002_2.height = 140.0, 100.0
    group_input_014_1.width, group_input_014_1.height = 140.0, 100.0
    compare_001_1.width, compare_001_1.height = 140.0, 100.0
    capture_attribute_004.width, capture_attribute_004.height = 140.0, 100.0
    normal_005.width, normal_005.height = 140.0, 100.0
    group_input_015.width, group_input_015.height = 140.0, 100.0
    capture_attribute_005.width, capture_attribute_005.height = 140.0, 100.0
    normal_006.width, normal_006.height = 140.0, 100.0
    group_input_016.width, group_input_016.height = 140.0, 100.0
    sample_nearest_surface_001.width, sample_nearest_surface_001.height = 150.0, 100.0
    delete_geometry_1.width, delete_geometry_1.height = 140.0, 100.0
    compare_002_1.width, compare_002_1.height = 140.0, 100.0
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    mesh_boolean_001.width, mesh_boolean_001.height = 140.0, 100.0
    group_input_017.width, group_input_017.height = 140.0, 100.0
    transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
    group_input_018.width, group_input_018.height = 140.0, 100.0
    object_info_002.width, object_info_002.height = 140.0, 100.0
    convex_hull.width, convex_hull.height = 140.0, 100.0
    compare_003_1.width, compare_003_1.height = 140.0, 100.0
    reroute_018.width, reroute_018.height = 16.0, 100.0
    attribute_statistic_001.width, attribute_statistic_001.height = 140.0, 100.0
    object_info_003.width, object_info_003.height = 140.0, 100.0
    is_shade_smooth.width, is_shade_smooth.height = 140.0, 100.0
    group_input_019.width, group_input_019.height = 140.0, 100.0
    compare_004_1.width, compare_004_1.height = 140.0, 100.0
    reroute_019.width, reroute_019.height = 16.0, 100.0
    group_input_020.width, group_input_020.height = 140.0, 100.0
    vector_math_019.width, vector_math_019.height = 140.0, 100.0
    group_001.width, group_001.height = 140.0, 100.0
    set_shade_smooth_1.width, set_shade_smooth_1.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    switch_001_1.width, switch_001_1.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    switch_002_1.width, switch_002_1.height = 140.0, 100.0
    reroute_020.width, reroute_020.height = 16.0, 100.0
    vector_math_020.width, vector_math_020.height = 140.0, 100.0
    group_input_021.width, group_input_021.height = 140.0, 100.0
    position_001_1.width, position_001_1.height = 140.0, 100.0
    sample_nearest_surface_002.width, sample_nearest_surface_002.height = 150.0, 100.0
    reroute_021.width, reroute_021.height = 16.0, 100.0
    vector_math_021.width, vector_math_021.height = 140.0, 100.0
    reroute_022.width, reroute_022.height = 16.0, 100.0
    reroute_023.width, reroute_023.height = 16.0, 100.0
    reroute_024.width, reroute_024.height = 16.0, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0
    reroute_005_2.width, reroute_005_2.height = 16.0, 100.0
    reroute_026.width, reroute_026.height = 16.0, 100.0
    reroute_004_2.width, reroute_004_2.height = 16.0, 100.0
    switch_1.width, switch_1.height = 140.0, 100.0
    group_input_3.width, group_input_3.height = 140.0, 100.0
    mesh_boolean_002.width, mesh_boolean_002.height = 140.0, 100.0
    reroute_025.width, reroute_025.height = 16.0, 100.0
    reroute_028.width, reroute_028.height = 16.0, 100.0
    group_output_3.width, group_output_3.height = 140.0, 100.0
    raycast_001.width, raycast_001.height = 150.0, 100.0
    align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
    vector_math_022.width, vector_math_022.height = 140.0, 100.0
    vector_math_023.width, vector_math_023.height = 140.0, 100.0
    group_input_022.width, group_input_022.height = 140.0, 100.0
    raycast.width, raycast.height = 150.0, 100.0
    extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
    set_position_1.width, set_position_1.height = 140.0, 100.0
    set_position_003.width, set_position_003.height = 140.0, 100.0
    rotation_to_euler.width, rotation_to_euler.height = 140.0, 100.0
    euler_to_rotation.width, euler_to_rotation.height = 140.0, 100.0
    group_002.width, group_002.height = 140.0, 100.0
    group_input_024.width, group_input_024.height = 140.0, 100.0
    vector_math_024.width, vector_math_024.height = 140.0, 100.0
    set_material_1.width, set_material_1.height = 140.0, 100.0

    # initialize hole links
    # group_input_001_1.peg -> object_info.Object
    hole.links.new(group_input_001_1.outputs[2], object_info.inputs[0])
    # position_1.Position -> attribute_statistic.Attribute
    hole.links.new(position_1.outputs[0], attribute_statistic.inputs[2])
    # position_001_1.Position -> sample_nearest_surface_002.Value
    hole.links.new(position_001_1.outputs[0], sample_nearest_surface_002.inputs[1])
    # object_info_001.Location -> sample_nearest_surface.Sample Position
    hole.links.new(object_info_001.outputs[1], sample_nearest_surface.inputs[3])
    # normal_002.Normal -> sample_nearest_surface.Value
    hole.links.new(normal_002.outputs[0], sample_nearest_surface.inputs[1])
    # reroute_2.Output -> align_euler_to_vector.Vector
    hole.links.new(reroute_2.outputs[0], align_euler_to_vector.inputs[2])
    # group_input_021.Geometry -> sample_nearest_surface_002.Mesh
    hole.links.new(group_input_021.outputs[0], sample_nearest_surface_002.inputs[0])
    # align_euler_to_vector.Rotation -> transform_geometry_1.Rotation
    hole.links.new(align_euler_to_vector.outputs[0], transform_geometry_1.inputs[2])
    # align_euler_to_vector.Rotation -> vector_rotate.Rotation
    hole.links.new(align_euler_to_vector.outputs[0], vector_rotate.inputs[4])
    # vector_rotate.Vector -> vector_math_001_2.Vector
    hole.links.new(vector_rotate.outputs[0], vector_math_001_2.inputs[0])
    # group_input_005_1.hole_position_handle -> object_info_001.Object
    hole.links.new(group_input_005_1.outputs[3], object_info_001.inputs[0])
    # vector_math_2.Vector -> vector_rotate.Vector
    hole.links.new(vector_math_2.outputs[0], vector_rotate.inputs[0])
    # attribute_statistic.Min -> vector_math_2.Vector
    hole.links.new(attribute_statistic.outputs[3], vector_math_2.inputs[0])
    # vector_math_001_2.Vector -> transform_geometry_1.Translation
    hole.links.new(vector_math_001_2.outputs[0], transform_geometry_1.inputs[1])
    # attribute_statistic.Range -> reroute_009.Input
    hole.links.new(attribute_statistic.outputs[5], reroute_009.inputs[0])
    # reroute_011.Output -> transform_geometry_001.Geometry
    hole.links.new(reroute_011.outputs[0], transform_geometry_001.inputs[0])
    # separate_xyz_1.Z -> reroute_010.Input
    hole.links.new(separate_xyz_1.outputs[2], reroute_010.inputs[0])
    # reroute_009.Output -> separate_xyz_1.Vector
    hole.links.new(reroute_009.outputs[0], separate_xyz_1.inputs[0])
    # group_input_002_1.random_seed -> random_value_1.Seed
    hole.links.new(group_input_002_1.outputs[1], random_value_1.inputs[8])
    # integer_1.Integer -> random_value_1.ID
    hole.links.new(integer_1.outputs[0], random_value_1.inputs[7])
    # group_input_003_1.hole_depth_factor_min -> random_value_1.Min
    hole.links.new(group_input_003_1.outputs[10], random_value_1.inputs[2])
    # reroute_010.Output -> math_3.Value
    hole.links.new(reroute_010.outputs[0], math_3.inputs[1])
    # random_value_1.Value -> math_3.Value
    hole.links.new(random_value_1.outputs[1], math_3.inputs[0])
    # normal_005.Normal -> capture_attribute_004.Value
    hole.links.new(normal_005.outputs[0], capture_attribute_004.inputs[1])
    # group_input_015.wall_include_bottom -> switch_002_1.Switch
    hole.links.new(group_input_015.outputs[16], switch_002_1.inputs[0])
    # mesh_boolean.Mesh -> mesh_boolean_001.Mesh
    hole.links.new(mesh_boolean.outputs[0], mesh_boolean_001.inputs[1])
    # switch_002_1.Output -> mesh_boolean.Mesh 1
    hole.links.new(switch_002_1.outputs[0], mesh_boolean.inputs[0])
    # reroute_006_2.Output -> reroute_005_2.Input
    hole.links.new(reroute_006_2.outputs[0], reroute_005_2.inputs[0])
    # reroute_019.Output -> compare_001_1.B
    hole.links.new(reroute_019.outputs[0], compare_001_1.inputs[5])
    # capture_attribute_004.Value -> compare_001_1.A
    hole.links.new(capture_attribute_004.outputs[1], compare_001_1.inputs[4])
    # reroute_002_2.Output -> reroute_003_2.Input
    hole.links.new(reroute_002_2.outputs[0], reroute_003_2.inputs[0])
    # reroute_001_2.Output -> reroute_002_2.Input
    hole.links.new(reroute_001_2.outputs[0], reroute_002_2.inputs[0])
    # normal_1.Normal -> capture_attribute.Value
    hole.links.new(normal_1.outputs[0], capture_attribute.inputs[1])
    # capture_attribute.Value -> compare_003_1.A
    hole.links.new(capture_attribute.outputs[1], compare_003_1.inputs[4])
    # transform_geometry_001.Geometry -> capture_attribute.Geometry
    hole.links.new(transform_geometry_001.outputs[0], capture_attribute.inputs[0])
    # reroute_020.Output -> reroute_007_2.Input
    hole.links.new(reroute_020.outputs[0], reroute_007_2.inputs[0])
    # transform_geometry_1.Geometry -> reroute_011.Input
    hole.links.new(transform_geometry_1.outputs[0], reroute_011.inputs[0])
    # reroute_005_2.Output -> reroute_019.Input
    hole.links.new(reroute_005_2.outputs[0], reroute_019.inputs[0])
    # set_position_1.Geometry -> reroute_004_2.Input
    hole.links.new(set_position_1.outputs[0], reroute_004_2.inputs[0])
    # group_input_007_1.random_seed -> random_value_001_1.Seed
    hole.links.new(group_input_007_1.outputs[1], random_value_001_1.inputs[8])
    # integer_001_1.Integer -> random_value_001_1.ID
    hole.links.new(integer_001_1.outputs[0], random_value_001_1.inputs[7])
    # group_input_003_1.hole_depth_factor_max -> random_value_1.Max
    hole.links.new(group_input_003_1.outputs[11], random_value_1.inputs[3])
    # group_input_006_1.hole_position_offset_max -> random_value_001_1.Max
    hole.links.new(group_input_006_1.outputs[5], random_value_001_1.inputs[1])
    # group_input_006_1.hole_position_offset_min -> random_value_001_1.Min
    hole.links.new(group_input_006_1.outputs[4], random_value_001_1.inputs[0])
    # object_info_001.Location -> vector_math_012.Vector
    hole.links.new(object_info_001.outputs[1], vector_math_012.inputs[0])
    # sample_nearest_surface.Value -> group.input_z
    hole.links.new(sample_nearest_surface.outputs[0], group.inputs[0])
    # random_value_001_1.Value -> separate_xyz_001.Vector
    hole.links.new(random_value_001_1.outputs[0], separate_xyz_001.inputs[0])
    # separate_xyz_001.X -> combine_xyz_001.X
    hole.links.new(separate_xyz_001.outputs[0], combine_xyz_001.inputs[0])
    # combine_xyz_001.Vector -> vector_math_010.Vector
    hole.links.new(combine_xyz_001.outputs[0], vector_math_010.inputs[1])
    # group.output_x -> vector_math_010.Vector
    hole.links.new(group.outputs[0], vector_math_010.inputs[0])
    # vector_math_010.Vector -> vector_math_009.Vector
    hole.links.new(vector_math_010.outputs[0], vector_math_009.inputs[0])
    # combine_xyz_2.Vector -> vector_math_011.Vector
    hole.links.new(combine_xyz_2.outputs[0], vector_math_011.inputs[1])
    # separate_xyz_001.Y -> combine_xyz_2.Y
    hole.links.new(separate_xyz_001.outputs[1], combine_xyz_2.inputs[1])
    # group.output_y -> vector_math_011.Vector
    hole.links.new(group.outputs[1], vector_math_011.inputs[0])
    # vector_math_011.Vector -> vector_math_009.Vector
    hole.links.new(vector_math_011.outputs[0], vector_math_009.inputs[1])
    # vector_math_009.Vector -> vector_math_012.Vector
    hole.links.new(vector_math_009.outputs[0], vector_math_012.inputs[1])
    # vector_math_012.Vector -> sample_nearest_surface_002.Sample Position
    hole.links.new(vector_math_012.outputs[0], sample_nearest_surface_002.inputs[3])
    # group_input_008_1.random_seed -> random_value_002_1.Seed
    hole.links.new(group_input_008_1.outputs[1], random_value_002_1.inputs[8])
    # integer_002_1.Integer -> random_value_002_1.ID
    hole.links.new(integer_002_1.outputs[0], random_value_002_1.inputs[7])
    # group_input_009_1.hole_orientation_offset_min -> random_value_002_1.Min
    hole.links.new(group_input_009_1.outputs[6], random_value_002_1.inputs[0])
    # group_input_009_1.hole_orientation_offset_max -> random_value_002_1.Max
    hole.links.new(group_input_009_1.outputs[7], random_value_002_1.inputs[1])
    # vector_math_012.Vector -> vector_rotate_001.Center
    hole.links.new(vector_math_012.outputs[0], vector_rotate_001.inputs[1])
    # normal_006.Normal -> sample_nearest_surface_001.Value
    hole.links.new(normal_006.outputs[0], sample_nearest_surface_001.inputs[1])
    # vector_math_008.Vector -> vector_rotate_001.Rotation
    hole.links.new(vector_math_008.outputs[0], vector_rotate_001.inputs[4])
    # reroute_014.Output -> vector_math_008.Vector
    hole.links.new(reroute_014.outputs[0], vector_math_008.inputs[0])
    # random_value_002_1.Value -> vector_math_008.Vector
    hole.links.new(random_value_002_1.outputs[0], vector_math_008.inputs[1])
    # rotation_to_euler.Euler -> reroute_014.Input
    hole.links.new(rotation_to_euler.outputs[0], reroute_014.inputs[0])
    # sample_nearest_surface.Value -> reroute_015.Input
    hole.links.new(sample_nearest_surface.outputs[0], reroute_015.inputs[0])
    # reroute_021.Output -> reroute_020.Input
    hole.links.new(reroute_021.outputs[0], reroute_020.inputs[0])
    # vector_math_021.Vector -> reroute_023.Input
    hole.links.new(vector_math_021.outputs[0], reroute_023.inputs[0])
    # sample_nearest_surface_002.Value -> reroute_022.Input
    hole.links.new(sample_nearest_surface_002.outputs[0], reroute_022.inputs[0])
    # group_input_010_1.Geometry -> sample_nearest_surface.Mesh
    hole.links.new(group_input_010_1.outputs[0], sample_nearest_surface.inputs[0])
    # vector_rotate_001.Vector -> reroute_021.Input
    hole.links.new(vector_rotate_001.outputs[0], reroute_021.inputs[0])
    # reroute_023.Output -> reroute_2.Input
    hole.links.new(reroute_023.outputs[0], reroute_2.inputs[0])
    # reroute_022.Output -> reroute_001_2.Input
    hole.links.new(reroute_022.outputs[0], reroute_001_2.inputs[0])
    # reroute_001_2.Output -> vector_math_001_2.Vector
    hole.links.new(reroute_001_2.outputs[0], vector_math_001_2.inputs[1])
    # reroute_2.Output -> reroute_008_1.Input
    hole.links.new(reroute_2.outputs[0], reroute_008_1.inputs[0])
    # reroute_008_1.Output -> vector_math_020.Vector
    hole.links.new(reroute_008_1.outputs[0], vector_math_020.inputs[0])
    # group_input_016.Geometry -> sample_nearest_surface_001.Mesh
    hole.links.new(group_input_016.outputs[0], sample_nearest_surface_001.inputs[0])
    # capture_attribute_005.Geometry -> delete_geometry_1.Geometry
    hole.links.new(capture_attribute_005.outputs[0], delete_geometry_1.inputs[0])
    # sample_nearest_surface_001.Value -> compare_002_1.B
    hole.links.new(sample_nearest_surface_001.outputs[0], compare_002_1.inputs[5])
    # capture_attribute_005.Value -> compare_002_1.A
    hole.links.new(capture_attribute_005.outputs[1], compare_002_1.inputs[4])
    # compare_002_1.Result -> delete_geometry_1.Selection
    hole.links.new(compare_002_1.outputs[0], delete_geometry_1.inputs[1])
    # delete_geometry_1.Geometry -> mesh_boolean.Mesh 2
    hole.links.new(delete_geometry_1.outputs[0], mesh_boolean.inputs[1])
    # group_input_016.Geometry -> capture_attribute_005.Geometry
    hole.links.new(group_input_016.outputs[0], capture_attribute_005.inputs[0])
    # normal_006.Normal -> capture_attribute_005.Value
    hole.links.new(normal_006.outputs[0], capture_attribute_005.inputs[1])
    # reroute_021.Output -> vector_math_021.Vector
    hole.links.new(reroute_021.outputs[0], vector_math_021.inputs[0])
    # reroute_015.Output -> vector_rotate_001.Vector
    hole.links.new(reroute_015.outputs[0], vector_rotate_001.inputs[0])
    # reroute_003_2.Output -> sample_nearest_surface_001.Sample Position
    hole.links.new(reroute_003_2.outputs[0], sample_nearest_surface_001.inputs[3])
    # reroute_007_2.Output -> reroute_006_2.Input
    hole.links.new(reroute_007_2.outputs[0], reroute_006_2.inputs[0])
    # vector_math_004.Vector -> set_position_1.Offset
    hole.links.new(vector_math_004.outputs[0], set_position_1.inputs[3])
    # math_001_3.Value -> vector_math_004.Scale
    hole.links.new(math_001_3.outputs[0], vector_math_004.inputs[3])
    # group_input_004_1.hole_size_tolerance -> math_001_3.Value
    hole.links.new(group_input_004_1.outputs[12], math_001_3.inputs[0])
    # normal_001_1.Normal -> capture_attribute_001.Value
    hole.links.new(normal_001_1.outputs[0], capture_attribute_001.inputs[1])
    # set_shade_smooth_1.Geometry -> capture_attribute_001.Geometry
    hole.links.new(set_shade_smooth_1.outputs[0], capture_attribute_001.inputs[0])
    # reroute_012.Output -> set_position_1.Geometry
    hole.links.new(reroute_012.outputs[0], set_position_1.inputs[0])
    # capture_attribute_004.Geometry -> switch_002_1.False
    hole.links.new(capture_attribute_004.outputs[0], switch_002_1.inputs[1])
    # mesh_boolean_001.Mesh -> switch_1.True
    hole.links.new(mesh_boolean_001.outputs[0], switch_1.inputs[2])
    # group_input_3.Geometry -> switch_1.False
    hole.links.new(group_input_3.outputs[0], switch_1.inputs[1])
    # group_input_3.wall_enable -> switch_1.Switch
    hole.links.new(group_input_3.outputs[13], switch_1.inputs[0])
    # vector_math_014.Vector -> set_position_001.Offset
    hole.links.new(vector_math_014.outputs[0], set_position_001.inputs[3])
    # normal_004.Normal -> capture_attribute_003.Value
    hole.links.new(normal_004.outputs[0], capture_attribute_003.inputs[1])
    # reroute_016.Output -> set_position_001.Geometry
    hole.links.new(reroute_016.outputs[0], set_position_001.inputs[0])
    # vector_math_015.Vector -> vector_math_014.Vector
    hole.links.new(vector_math_015.outputs[0], vector_math_014.inputs[0])
    # group_input_014_1.wall_thickness -> math_002_2.Value
    hole.links.new(group_input_014_1.outputs[15], math_002_2.inputs[1])
    # math_002_2.Value -> vector_math_014.Scale
    hole.links.new(math_002_2.outputs[0], vector_math_014.inputs[3])
    # set_position_001.Geometry -> capture_attribute_004.Geometry
    hole.links.new(set_position_001.outputs[0], capture_attribute_004.inputs[0])
    # capture_attribute_003.Geometry -> reroute_016.Input
    hole.links.new(capture_attribute_003.outputs[0], reroute_016.inputs[0])
    # capture_attribute_001.Geometry -> reroute_012.Input
    hole.links.new(capture_attribute_001.outputs[0], reroute_012.inputs[0])
    # reroute_007_2.Output -> vector_math_002.Vector
    hole.links.new(reroute_007_2.outputs[0], vector_math_002.inputs[0])
    # math_3.Value -> vector_math_002.Scale
    hole.links.new(math_3.outputs[0], vector_math_002.inputs[3])
    # vector_math_002.Vector -> transform_geometry_001.Translation
    hole.links.new(vector_math_002.outputs[0], transform_geometry_001.inputs[1])
    # set_position_002.Geometry -> switch_002_1.True
    hole.links.new(set_position_002.outputs[0], switch_002_1.inputs[2])
    # reroute_010.Output -> vector_math_020.Scale
    hole.links.new(reroute_010.outputs[0], vector_math_020.inputs[3])
    # reroute_017.Output -> vector_math_018.Vector
    hole.links.new(reroute_017.outputs[0], vector_math_018.inputs[1])
    # capture_attribute_003.Value -> vector_math_018.Vector
    hole.links.new(capture_attribute_003.outputs[1], vector_math_018.inputs[0])
    # capture_attribute_003.Value -> vector_math_016.Vector
    hole.links.new(capture_attribute_003.outputs[1], vector_math_016.inputs[0])
    # vector_math_016.Vector -> vector_math_015.Vector
    hole.links.new(vector_math_016.outputs[0], vector_math_015.inputs[0])
    # reroute_017.Output -> vector_math_017.Vector
    hole.links.new(reroute_017.outputs[0], vector_math_017.inputs[0])
    # vector_math_017.Vector -> vector_math_016.Vector
    hole.links.new(vector_math_017.outputs[0], vector_math_016.inputs[1])
    # vector_math_018.Value -> vector_math_017.Scale
    hole.links.new(vector_math_018.outputs[1], vector_math_017.inputs[3])
    # vector_math_006.Vector -> vector_math_003.Vector
    hole.links.new(vector_math_006.outputs[0], vector_math_003.inputs[0])
    # vector_math_007.Vector -> vector_math_006.Vector
    hole.links.new(vector_math_007.outputs[0], vector_math_006.inputs[1])
    # vector_math_005.Value -> vector_math_007.Scale
    hole.links.new(vector_math_005.outputs[1], vector_math_007.inputs[3])
    # vector_math_003.Vector -> vector_math_004.Vector
    hole.links.new(vector_math_003.outputs[0], vector_math_004.inputs[0])
    # capture_attribute_001.Value -> vector_math_005.Vector
    hole.links.new(capture_attribute_001.outputs[1], vector_math_005.inputs[0])
    # reroute_013.Output -> vector_math_005.Vector
    hole.links.new(reroute_013.outputs[0], vector_math_005.inputs[1])
    # reroute_013.Output -> vector_math_007.Vector
    hole.links.new(reroute_013.outputs[0], vector_math_007.inputs[0])
    # reroute_006_2.Output -> reroute_017.Input
    hole.links.new(reroute_006_2.outputs[0], reroute_017.inputs[0])
    # reroute_006_2.Output -> reroute_013.Input
    hole.links.new(reroute_006_2.outputs[0], reroute_013.inputs[0])
    # math_001_3.Value -> math_002_2.Value
    hole.links.new(math_001_3.outputs[0], math_002_2.inputs[0])
    # convex_hull.Convex Hull -> transform_geometry_003.Geometry
    hole.links.new(convex_hull.outputs[0], transform_geometry_003.inputs[0])
    # transform_geometry_003.Geometry -> transform_geometry_002.Geometry
    hole.links.new(transform_geometry_003.outputs[0], transform_geometry_002.inputs[0])
    # vector_math_002.Vector -> transform_geometry_002.Translation
    hole.links.new(vector_math_002.outputs[0], transform_geometry_002.inputs[1])
    # vector_math_001_2.Vector -> transform_geometry_003.Translation
    hole.links.new(vector_math_001_2.outputs[0], transform_geometry_003.inputs[1])
    # align_euler_to_vector.Rotation -> transform_geometry_003.Rotation
    hole.links.new(align_euler_to_vector.outputs[0], transform_geometry_003.inputs[2])
    # is_shade_smooth.Smooth -> attribute_statistic_001.Attribute
    hole.links.new(is_shade_smooth.outputs[0], attribute_statistic_001.inputs[2])
    # attribute_statistic_001.Median -> set_shade_smooth_1.Shade Smooth
    hole.links.new(attribute_statistic_001.outputs[1], set_shade_smooth_1.inputs[2])
    # capture_attribute_001.Value -> vector_math_006.Vector
    hole.links.new(capture_attribute_001.outputs[1], vector_math_006.inputs[0])
    # normal_003.Normal -> capture_attribute_002.Value
    hole.links.new(normal_003.outputs[0], capture_attribute_002.inputs[1])
    # capture_attribute_002.Value -> compare_1.A
    hole.links.new(capture_attribute_002.outputs[1], compare_1.inputs[4])
    # capture_attribute_002.Geometry -> extrude_mesh.Mesh
    hole.links.new(capture_attribute_002.outputs[0], extrude_mesh.inputs[0])
    # compare_1.Result -> extrude_mesh.Selection
    hole.links.new(compare_1.outputs[0], extrude_mesh.inputs[1])
    # vector_math_013.Vector -> extrude_mesh.Offset
    hole.links.new(vector_math_013.outputs[0], extrude_mesh.inputs[2])
    # reroute_008_1.Output -> vector_math_013.Vector
    hole.links.new(reroute_008_1.outputs[0], vector_math_013.inputs[0])
    # reroute_010.Output -> vector_math_013.Scale
    hole.links.new(reroute_010.outputs[0], vector_math_013.inputs[3])
    # transform_geometry_002.Geometry -> capture_attribute_002.Geometry
    hole.links.new(transform_geometry_002.outputs[0], capture_attribute_002.inputs[0])
    # set_shade_smooth_1.Geometry -> switch_001_1.False
    hole.links.new(set_shade_smooth_1.outputs[0], switch_001_1.inputs[1])
    # switch_001_1.Output -> capture_attribute_003.Geometry
    hole.links.new(switch_001_1.outputs[0], capture_attribute_003.inputs[0])
    # group_input_013_1.wall_remove_inner_holes -> switch_001_1.Switch
    hole.links.new(group_input_013_1.outputs[14], switch_001_1.inputs[0])
    # reroute_018.Output -> compare_003_1.B
    hole.links.new(reroute_018.outputs[0], compare_003_1.inputs[5])
    # reroute_008_1.Output -> compare_1.B
    hole.links.new(reroute_008_1.outputs[0], compare_1.inputs[5])
    # extrude_mesh.Mesh -> switch_001_1.True
    hole.links.new(extrude_mesh.outputs[0], switch_001_1.inputs[2])
    # group_input_011_1.random_seed -> random_value_003_1.Seed
    hole.links.new(group_input_011_1.outputs[1], random_value_003_1.inputs[8])
    # integer_003_1.Integer -> random_value_003_1.ID
    hole.links.new(integer_003_1.outputs[0], random_value_003_1.inputs[7])
    # random_value_003_1.Value -> combine_xyz_002.Z
    hole.links.new(random_value_003_1.outputs[1], combine_xyz_002.inputs[2])
    # combine_xyz_002.Vector -> euler_to_rotation.Euler
    hole.links.new(combine_xyz_002.outputs[0], euler_to_rotation.inputs[0])
    # group_input_018.peg -> object_info_002.Object
    hole.links.new(group_input_018.outputs[2], object_info_002.inputs[0])
    # group_001.Geometry -> transform_geometry_004.Geometry
    hole.links.new(group_001.outputs[0], transform_geometry_004.inputs[0])
    # group_input_012_1.hole_insertion_angle_min -> random_value_003_1.Min
    hole.links.new(group_input_012_1.outputs[8], random_value_003_1.inputs[2])
    # group_input_012_1.hole_insertion_angle_max -> random_value_003_1.Max
    hole.links.new(group_input_012_1.outputs[9], random_value_003_1.inputs[3])
    # transform_geometry_004.Geometry -> transform_geometry_1.Geometry
    hole.links.new(transform_geometry_004.outputs[0], transform_geometry_1.inputs[0])
    # transform_geometry_004.Geometry -> convex_hull.Geometry
    hole.links.new(transform_geometry_004.outputs[0], convex_hull.inputs[0])
    # group_input_019.peg -> object_info_003.Object
    hole.links.new(group_input_019.outputs[2], object_info_003.inputs[0])
    # capture_attribute.Value -> compare_004_1.A
    hole.links.new(capture_attribute.outputs[1], compare_004_1.inputs[4])
    # compare_003_1.Result -> boolean_math.Boolean
    hole.links.new(compare_003_1.outputs[0], boolean_math.inputs[1])
    # compare_004_1.Result -> boolean_math.Boolean
    hole.links.new(compare_004_1.outputs[0], boolean_math.inputs[0])
    # reroute_008_1.Output -> reroute_018.Input
    hole.links.new(reroute_008_1.outputs[0], reroute_018.inputs[0])
    # reroute_018.Output -> compare_004_1.B
    hole.links.new(reroute_018.outputs[0], compare_004_1.inputs[5])
    # capture_attribute_004.Geometry -> set_position_002.Geometry
    hole.links.new(capture_attribute_004.outputs[0], set_position_002.inputs[0])
    # compare_001_1.Result -> set_position_002.Selection
    hole.links.new(compare_001_1.outputs[0], set_position_002.inputs[1])
    # group_input_020.wall_thickness -> vector_math_019.Scale
    hole.links.new(group_input_020.outputs[15], vector_math_019.inputs[3])
    # reroute_019.Output -> vector_math_019.Vector
    hole.links.new(reroute_019.outputs[0], vector_math_019.inputs[0])
    # vector_math_024.Vector -> set_position_002.Offset
    hole.links.new(vector_math_024.outputs[0], set_position_002.inputs[3])
    # reroute_026.Output -> vector_math_022.Vector
    hole.links.new(reroute_026.outputs[0], vector_math_022.inputs[1])
    # vector_math_002.Vector -> reroute_024.Input
    hole.links.new(vector_math_002.outputs[0], reroute_024.inputs[0])
    # reroute_024.Output -> reroute_025.Input
    hole.links.new(reroute_024.outputs[0], reroute_025.inputs[0])
    # set_material_1.Geometry -> group_output_3.Geometry
    hole.links.new(set_material_1.outputs[0], group_output_3.inputs[0])
    # reroute_022.Output -> vector_math_022.Vector
    hole.links.new(reroute_022.outputs[0], vector_math_022.inputs[0])
    # reroute_023.Output -> reroute_026.Input
    hole.links.new(reroute_023.outputs[0], reroute_026.inputs[0])
    # group_input_022.Geometry -> raycast.Target Geometry
    hole.links.new(group_input_022.outputs[0], raycast.inputs[0])
    # reroute_026.Output -> vector_math_023.Vector
    hole.links.new(reroute_026.outputs[0], vector_math_023.inputs[0])
    # vector_math_023.Vector -> raycast.Ray Direction
    hole.links.new(vector_math_023.outputs[0], raycast.inputs[3])
    # vector_math_022.Vector -> raycast.Source Position
    hole.links.new(vector_math_022.outputs[0], raycast.inputs[2])
    # raycast.Hit Position -> group_output_3.entrance_position
    hole.links.new(raycast.outputs[1], group_output_3.inputs[1])
    # combine_xyz_002.Vector -> reroute_028.Input
    hole.links.new(combine_xyz_002.outputs[0], reroute_028.inputs[0])
    # mesh_boolean_002.Mesh -> raycast_001.Target Geometry
    hole.links.new(mesh_boolean_002.outputs[0], raycast_001.inputs[0])
    # reroute_025.Output -> raycast_001.Ray Direction
    hole.links.new(reroute_025.outputs[0], raycast_001.inputs[3])
    # raycast.Hit Position -> raycast_001.Source Position
    hole.links.new(raycast.outputs[1], raycast_001.inputs[2])
    # raycast_001.Hit Normal -> align_euler_to_vector_001.Vector
    hole.links.new(raycast_001.outputs[2], align_euler_to_vector_001.inputs[2])
    # reroute_028.Output -> align_euler_to_vector_001.Rotation
    hole.links.new(reroute_028.outputs[0], align_euler_to_vector_001.inputs[0])
    # reroute_028.Output -> group_output_3.entrance_orientation
    hole.links.new(reroute_028.outputs[0], group_output_3.inputs[2])
    # align_euler_to_vector_001.Rotation -> group_output_3.bottom_orientation
    hole.links.new(align_euler_to_vector_001.outputs[0], group_output_3.inputs[4])
    # raycast_001.Hit Position -> group_output_3.bottom_position
    hole.links.new(raycast_001.outputs[1], group_output_3.inputs[3])
    # capture_attribute.Geometry -> set_position_003.Geometry
    hole.links.new(capture_attribute.outputs[0], set_position_003.inputs[0])
    # compare_003_1.Result -> set_position_003.Selection
    hole.links.new(compare_003_1.outputs[0], set_position_003.inputs[1])
    # vector_math_020.Vector -> set_position_003.Offset
    hole.links.new(vector_math_020.outputs[0], set_position_003.inputs[3])
    # set_position_003.Geometry -> set_shade_smooth_1.Geometry
    hole.links.new(set_position_003.outputs[0], set_shade_smooth_1.inputs[0])
    # boolean_math.Boolean -> set_shade_smooth_1.Selection
    hole.links.new(boolean_math.outputs[0], set_shade_smooth_1.inputs[1])
    # object_info_001.Rotation -> rotation_to_euler.Rotation
    hole.links.new(object_info_001.outputs[2], rotation_to_euler.inputs[0])
    # euler_to_rotation.Rotation -> transform_geometry_004.Rotation
    hole.links.new(euler_to_rotation.outputs[0], transform_geometry_004.inputs[2])
    # group_002.Geometry -> attribute_statistic.Geometry
    hole.links.new(group_002.outputs[0], attribute_statistic.inputs[0])
    # group_002.Geometry -> attribute_statistic_001.Geometry
    hole.links.new(group_002.outputs[0], attribute_statistic_001.inputs[0])
    # group_002.Geometry -> group_001.Geometry
    hole.links.new(group_002.outputs[0], group_001.inputs[0])
    # group_input_024.random_seed -> group_002.random_seed
    hole.links.new(group_input_024.outputs[1], group_002.inputs[0])
    # switch_1.Output -> mesh_boolean_002.Mesh 1
    hole.links.new(switch_1.outputs[0], mesh_boolean_002.inputs[0])
    # reroute_004_2.Output -> mesh_boolean_002.Mesh 2
    hole.links.new(reroute_004_2.outputs[0], mesh_boolean_002.inputs[1])
    # vector_math_019.Vector -> vector_math_024.Vector
    hole.links.new(vector_math_019.outputs[0], vector_math_024.inputs[0])
    # mesh_boolean_002.Mesh -> set_material_1.Geometry
    hole.links.new(mesh_boolean_002.outputs[0], set_material_1.inputs[0])
    # group_input_017.Geometry -> mesh_boolean_001.Mesh
    hole.links.new(group_input_017.outputs[0], mesh_boolean_001.inputs[1])
    return hole


hole = hole_node_group()
