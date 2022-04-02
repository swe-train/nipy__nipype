# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..io import BIDSDataGrabber


def test_BIDSDataGrabber_inputs():
    input_map = dict(
        base_dir=dict(
            mandatory=True,
        ),
        extra_derivatives=dict(),
        index_derivatives=dict(
            mandatory=True,
            usedefault=True,
        ),
        load_layout=dict(
            mandatory=False,
        ),
        output_query=dict(),
        raise_on_empty=dict(
            usedefault=True,
        ),
    )
    inputs = BIDSDataGrabber.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BIDSDataGrabber_outputs():
    output_map = dict()
    outputs = BIDSDataGrabber.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
