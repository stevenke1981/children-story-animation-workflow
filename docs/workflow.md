# Production workflow

## 1. Creative brief and identity

Agree on age range, language, duration, delivery format and content. For preschoolers, favor familiar actions, clear cause and effect and everyday settings when requested. Make a scene plan with cumulative timing and concise narration. For five minutes, ten roughly 30-second scenes are a useful starting point, not a substitute for timing the completed audio. Keep character designs and names consistent.

Identify the requested service, active login, project and any account-specific restrictions on the actual surface used. A browser login does not verify an API key. Do not treat an example email, avatar or past session as proof of account ownership. Keep credentials and account mappings private. If an explicitly required account cannot be verified, stop the dependent write and ask the user.

## 2. Visual references and Flow

Create a dedicated project when appropriate. Generate a character reference and environment reference, then numbered 16:9 storyboard stills, referencing the character sheet where supported. Download and visually inspect all stills; record observed inconsistencies instead of claiming identity is perfect.

For each shot, prepare a start frame and a compatible end frame showing the intended action's result. Select both in Flow's Frames mode through its supported interface when requested, and verify both appear before submitting. Existing clips made with a start frame alone may be reused only when the user authorizes them and they pass review. Check model, duration, resolution, output count, per-generation credit cost and balance from the current UI before submitting. A historical example used Veo 3.1 Lite, 720p, 8 seconds, four outputs for 40 credits, but current prices and availability must be rechecked. Save project URL, scene number, prompt, settings and job status in a private ledger. Submit each intended job once; inspect the original project if outcome is uncertain. Never retry a provider policy refusal by changing accounts or disguising the same request. Preserve a rejected shot as a reported gap.

Short variations derived from the same frame do not automatically form a continuous scene. Inspect actual clips for motion, continuity and transitions. When the user requires fully animated footage, storyboard stills are generation references only: do not replace a missing clip with a still, a pan or zoom over a still, or a held frame. Flag unusually still intervals for review; automated freeze detection alone does not establish creative quality. Use only material the user has authorized. Upload through the supported file chooser. If Chrome requests extension access to file URLs, have the user enable it; do not bypass the restriction.

For a continuous sequence, assign each shot its own consecutive frame pair: F00→F01, F01→F02, and so on. Reuse each exact ending image as the following shot's starting image, and create each next frame from the preceding reference while checking characters, props and composition. Forty shots need 41 boundary images; if the brief requests 42, document the extra image's specific transition or replacement role. Produce and inspect a short sample first when requested. Compare the actual adjacent clip endpoints as well as checking motion inside each clip; shared references do not by themselves guarantee seamless video.

Keep shot identifiers, bookkeeping and references to production steps in the local shot ledger, not in the generation prompt when the user requests clean prompts. Describe observable action, the characters and their positions, relevant objects, lighting and camera. The [Seedance 2.0 skill project](https://github.com/Emily2040/seedance-2.0) provides directing principles that can inform this writing, but it targets Seedance: adapt general craft to Flow/Veo rather than treating model-specific syntax or capabilities as interchangeable.

## 3. Narration and subtitles

For HeyGen voice, send Simplified Chinese text to `heygen/heygen-voice-1-turbo:free`; keep the subtitle text separately in the requested script. Generate English narration separately when requested. Check current live zero pricing and use only the exact free route unless the user has explicitly approved a specific paid model, price and cost ceiling. Check API identity independently of browser sessions. Generate one WAV per scene, check the actual files and durations, and preserve source text.

If requested, use `gpt-transcribe-mcp` to compare actual audio against the source. It sends recordings to OpenAI and may incur a charge: disclose the model, rate, estimate and ceiling, obtain payer approval, and stay within it. The tool supplies a transcript, not word timing or a guarantee of pronunciation. Actual listening or transcription not performed must be reported as NOT_RUN.

Prepare Simplified Chinese + English subtitles when requested. Translate meaningfully and time them against the actual voice recording; do not claim proportional timing is audio alignment. Use a readable CJK font with a verifiable license, for example [Iansui](https://github.com/ButTaiwan/iansui), preserving its OFL license. The final picture must remain readable on small screens.

## 4. Music and edit

Verify Suno’s active service account and download allowance. If the user requested Flow Music as fallback and Suno downloads are unavailable, verify the Flow Music account separately, generate instrumental music, and download only through the product. Do not buy credits or bypass a download restriction. Decode the resulting audio and record its duration; listening for suitability remains a separate check.

Assemble clips in scene order with narration, music at a level that does not mask speech, and timed bilingual subtitles. For shorter music, create a clean loop or transition. Keep separate language tracks or exports as requested. Verify duration, video/audio streams and text rendering; play the actual result and check pronunciation, audiovisual synchronization, readability and age suitability when human listening/viewing is available. Report every unperformed check and every incomplete asset honestly.

## 5. Publish or handoff

Review files and Git diff for secrets, private paths, account identifiers, copyrighted materials and unapproved media before any public push. A public repository of the workflow is not permission to publish the resulting film or user assets. Preserve provider receipts and private production state outside the repository. Include sources and license notices, exact test outcomes and recovery instructions.
