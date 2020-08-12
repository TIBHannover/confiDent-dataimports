import pytest
from dataimports.file_utils import yaml_get_source
from dataimports.tests import populateglobals
from dataimports.globals import (confid_mapping,
                                 invert_confid_map,)

if len(confid_mapping) == 0 and len(invert_confid_map) == 0:
    populateglobals.populateglobals()

# TODO: Test for integraty of confident_mapping.yml


@pytest.mark.mapping
def test_confid_mapping():
    sources = ['wikidata']
    for schema in sources:
        confid_mapping.update(
            yaml_get_source(f'{schema}/confident_mapping.yml'))
        confid_keys = list(confid_mapping.keys())
        confid_keys_set = list(set(confid_keys))

        external_props = [v['external_prop']
                          for k, v in confid_mapping.items() if
                          v and 'external_prop' in v.keys()
                          and v['external_prop']]

        assert len(external_props) > 0, \
            f"Expected mapping. {confid_mapping} is empty"

        assert sorted(confid_keys) == sorted(confid_keys_set),\
            f"Expected unique keys in mapping, Actual keys {confid_keys}"

        assert len(invert_confid_map) > 0

        confid_keys_in_inv_mapping = [v for v in invert_confid_map.values()]
        for k in confid_keys_in_inv_mapping:
            assert k in confid_keys,\
                f"confid key: {k} in inverted mapping is not in confid keys " \
                f"of {schema}"


@pytest.mark.mapping
def test_confid_mapping_yaml():
    sources = ['wikidata']
    for schema in sources:
        confid_mapping.clear()  # reset dict for each source
        confid_mapping.update(
            yaml_get_source(f'{schema}/confident_mapping.yml'))
        for k, value_dict in confid_mapping.items():
            assert 'range' in value_dict, \
                f"range: is missing from {schema}/confident_mapping.yml " \
                f"key: {k}"
