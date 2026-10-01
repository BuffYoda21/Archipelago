from collections.abc import Mapping
from pathlib import Path
from typing import Any
from Options import OptionSet

import re

from ..options import OoT3DChoice, OoT3DNamedRange, OoT3DOptions, OoT3DRange, OoT3DToggle


OPTION_TYPES = OoT3DOptions.type_hints
OPTION_CLASSES = (OoT3DChoice, OoT3DRange, OoT3DToggle, OoT3DNamedRange)
TEMPLATE_PATH = Path(__file__).parent.parent / "data" / "template.xml"
SETTING_PATTERN = re.compile(r'(<setting name="([^"]+)">)([^<]*)(</setting>)')


def _xml_value(value: Any) -> str:
	if isinstance(value, bool):
		return str(int(value))
	return str(value)

def options_to_xml(options: Mapping[str, Any]) -> str:
	option_groups_to_convert = options.values()
	if all(isinstance(option_group, Mapping) for option_group in option_groups_to_convert):
		option_groups_to_convert = (
			option for option_group in options.values() for option in option_group.items()
		)
	else:
		option_groups_to_convert = options.items()

	overrides = []
	for option_name, value in option_groups_to_convert:
		option_type = OPTION_TYPES.get(option_name)
		if option_type is not None and issubclass(option_type, OPTION_CLASSES):
			xml_name = option_type.xml_name or option_type.display_name
			if option_type.xml_offset:
				value += option_type.xml_offset
				if value < 0:
					value = 0
			overrides.append((xml_name, _xml_value(value), option_type.xml_duplicate_index))
		elif option_type is not None and issubclass(option_type, OptionSet):
			overrides.extend((option_key, "1", 0) for option_key in value)

	overrides_by_name = {}
	for option_name, value, duplicate_index in overrides:
		overrides_by_name.setdefault(option_name, []).append((value, duplicate_index))

	def replace_setting(match: re.Match[str]) -> str:
		setting_name = match.group(2)
		setting_overrides = overrides_by_name.get(setting_name)
		if setting_overrides:
			value, duplicate_index = setting_overrides[0]
			if duplicate_index:
				setting_overrides[0] = (value, duplicate_index - 1)
				return match.group(0)
			setting_overrides.pop(0)
			return f"{match.group(1)}{value}{match.group(4)}"
		return match.group(0)

	return SETTING_PATTERN.sub(replace_setting, TEMPLATE_PATH.read_text(encoding="utf-8"))