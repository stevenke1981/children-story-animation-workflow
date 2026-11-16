"""Validate a human- and agent-readable storyboard plan."""
import argparse
import json
import sys
from pathlib import Path


def validate(plan, root, check_assets=False):
    errors = []
    scenes = plan.get("scenes", [])
    target = plan.get("target_duration_seconds")
    if not isinstance(target, (int, float)) or isinstance(target, bool) or target <= 0:
        errors.append("target_duration_seconds must be positive")
    if not isinstance(scenes, list) or not scenes:
        return errors + ["scenes must be a nonempty list"]
    languages = plan.get("narration_languages", [])
    if not isinstance(languages, list) or not languages:
        errors.append("narration_languages must be a nonempty list")
        languages = []
    current = 0
    seen = set()
    for scene in scenes:
        if not isinstance(scene, dict):
            errors.append("each scene must be an object")
            continue
        name = scene.get("id")
        if not isinstance(name, str) or not name or name in seen:
            errors.append(f"invalid or duplicate scene id: {name!r}")
        else:
            seen.add(name)
        duration, start = scene.get("duration_seconds"), scene.get("start_seconds")
        if not isinstance(duration, (int, float)) or isinstance(duration, bool) or duration <= 0:
            errors.append(f"{name}: duration must be positive")
        elif not isinstance(start, (int, float)) or isinstance(start, bool) or abs(start - current) > 0.001:
            errors.append(f"{name}: expected start {current}, got {start!r}")
            current += duration
        else:
            current += duration
        narration = scene.get("narration", {})
        for language in languages:
            if not isinstance(narration, dict) or not isinstance(narration.get(language), str) or not narration[language].strip():
                errors.append(f"{name}: missing narration for {language}")
        for field in ("image", "video"):
            value = scene.get(field)
            if not isinstance(value, str) or not value:
                errors.append(f"{name}: missing {field} path")
                continue
            path = Path(value)
            if path.is_absolute() or not (root / path).resolve().is_relative_to(root.resolve()):
                errors.append(f"{name}: {field} must stay inside the plan directory")
            elif check_assets and not (root / path).is_file():
                errors.append(f"{name}: {field} file not found: {value}")
    if isinstance(target, (int, float)) and not isinstance(target, bool) and abs(current - target) > 0.001:
        errors.append(f"scene duration total {current} differs from target {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--check-assets", action="store_true")
    args = parser.parse_args()
    try:
        data = json.loads(args.plan.read_text(encoding="utf-8-sig"))
        if not isinstance(data, dict):
            raise ValueError("plan must be an object")
        errors = validate(data, args.plan.parent, args.check_assets)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {len(data['scenes'])} scenes, {data['target_duration_seconds']} seconds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
