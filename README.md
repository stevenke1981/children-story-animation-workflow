# Children’s Story Animation Workflow

A human-readable, agent-friendly workflow for creating a roughly five-minute children’s animation from a story. The editable plan describes scenes; Google Flow produces character art, scene art and short animated clips; HeyGen Voice Turbo on OpenRouter creates Simplified Chinese and English narration; Flow Music supplies instrumental music when a specified Suno account cannot download. Editing and final review remain explicit stages.

This is a **workflow and validation toolkit**, not a claim that a movie has already been generated. It does not automate login, bypass upload permissions, evade policy refusals, buy credits, publish generated media, or create accounts. Service UIs, capabilities, pricing and licensing change; verify them on the actual session before each operation.

## Start here

1. Read [the workflow](docs/workflow.md), including account, cost, approval and review boundaries.
2. Copy [the scene plan template](templates/story-plan.json) into a private production folder. Replace all placeholders and add scenes totaling the target duration.
3. Run `python scripts/validate_plan.py path/to/story-plan.json` before generating. Paths are relative to the plan file. Pass `--check-assets` only after files exist.
4. Follow the workflow stages and save dated evidence. A storyboard, prompt, processing job or successful API response alone is not a completed film.

## MCP servers and skills

| Use | Integration | Purpose |
| --- | --- | --- |
| Browser | Host-provided browser/computer-use connector | Use selected authenticated tabs and visible site controls; file-URL access may need the user to enable it. |
| Narration | [heygen-voice-mcp](https://github.com/stevenke1981/heygen-voice-mcp) | Exact free HeyGen TTS route, Simplified Chinese conversion and WAV output. |
| Speech check | [gpt-transcribe-mcp](https://github.com/stevenke1981/gpt-transcribe-mcp) | Optional paid OpenAI transcription with explicit consent; not a substitute for listening. |
| Flow video | `flow-video-generator` skill, if locally installed | Follow its installed instructions for Flow jobs, credit checks, account selection, and downloads. It is environment-specific and is not bundled here. |
| Transcription fallback | `qwen3asr` skill, if locally installed | Optional offline transcription where available, subject to user direction and actual model availability. |
| Local media | `soundx` MCP/skill or FFmpeg | Inspect, mix and render local files; verify that the chosen tools are available. |

A skill or MCP name in this table does not install it. Never copy credentials or account mappings into a public repo. Use the host’s actual documented setup and retain logs and media outside this repository by default.

## Validation

```sh
python -m unittest discover -s tests -v
python scripts/validate_plan.py templates/story-plan.json
```

The template is intentionally a 60-second two-scene example, not a five-minute deliverable. Set the target and scene list for the actual production. The validator checks structural consistency, timing, local path safety, and optional file existence; it does not check creative quality, speech alignment or rights.

## License

MIT for this repository’s code and documentation. Third-party software, fonts and generated material have their own licenses and terms. Confirm distribution and commercial-use rights before publishing a finished film.
