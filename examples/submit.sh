#!/usr/bin/env bash
set -euo pipefail
: "${MUAPI_API_KEY:?Set MUAPI_API_KEY first}"
curl --fail-with-body -sS -X POST https://api.muapi.ai/api/v1/runway-aleph-v2v \
  -H "Content-Type: application/json" \
  -H "x-api-key: $MUAPI_API_KEY" \
  -d '{"prompt": "Transform this samurai cliff scene into a neon cyberpunk style, glowing city skyline in the distance, rain-soaked ground with light reflections.", "video_url": "https://example.com/replace-with-your-file"}'
