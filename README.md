# Google Cloud Run service URL
https://safe-py-executor-498806096988.us-central1.run.app



# Example Requests
```bash
```
## 1. Word-count using only the Python standard library
curl -X POST https://safe-py-executor-498806096988.us-central1.run.app/execute \
  -H 'Content-Type: application/json' \
  -d '{"script":"def main():\n  text = \"The quick brown fox jumps over the lazy dog\"\n  words = text.split()\n  counts = {w: words.count(w) for w in set(words)}\n  return counts\n\nif __name__ == \"__main__\":\n import json; print(json.dumps(main()))"}'

```
{"result":{"The":1,"quick":1,"brown":1,"fox":1,"jumps":1,"over":1,"the":1,"lazy":1,"dog":1},"stdout":"{\"quick\": 1, \"fox\": 1, \"lazy\": 1, \"dog\": 1, \"brown\": 1, \"jumps\": 1, \"The\": 1, \"over\": 1, \"the\": 1}\n"}
```

## 2. Numpy array math
curl -X POST https://safe-py-executor-498806096988.us-central1.run.app/execute \
  -H 'Content-Type: application/json' \
  -d '{"script":"import numpy as np\n\ndef main():\n  a = np.arange(6).reshape(2, 3)\n  return {\"matrix\": a.tolist(), \"sum\": int(a.sum())}\n\nif __name__ == \"__main__\":\n import json; print(json.dumps(main()))"}'

```
{"result":{"matrix":[[0,1,2],[3,4,5]],"sum":15},"stdout":"{\"matrix\": [[0, 1, 2], [3, 4, 5]], \"sum\": 15}\n"}
```

## 3. Pandas describe statistics
curl -X POST https://safe-py-executor-498806096988.us-central1.run.app/execute \
  -H 'Content-Type: application/json' \
  -d '{"script":"import pandas as pd\n\ndef main():\n  df = pd.DataFrame({\"a\": [1, 2, 3], \"b\": [4, 5, 6]})\n  return df.describe().to_dict()\n\nif __name__ == \"__main__\":\n import json; print(json.dumps(main()))"}'

```
{"result":{"a":{"25%":1.5,"50%":2.0,"75%":2.5,"count":3.0,"max":3.0,"mean":2.0,"min":1.0,"std":1.0},"b":{"25%":4.5,"50%":5.0,"75%":5.5,"count":3.0,"max":6.0,"mean":5.0,"min":4.0,"std":1.0}},"stdout":"{\"a\": {\"count\": 3.0, \"mean\": 2.0, \"std\": 1.0, \"min\": 1.0, \"25%\": 1.5, \"50%\": 2.0, \"75%\": 2.5, \"max\": 3.0}, \"b\": {\"count\": 3.0, \"mean\": 5.0, \"std\": 1.0, \"min\": 4.0, \"25%\": 4.5, \"50%\": 5.0, \"75%\": 5.5, \"max\": 6.0}}\n"}
```

## 4. Script that prints to stdout (stdout is returned separately)
curl -X POST https://safe-py-executor-498806096988.us-central1.run.app/execute \
  -H 'Content-Type: application/json' \
  -d '{"script":"def main():\n  for i in range(3):\n    print(\"print\", i)\n  return {\"msg\": \"stdout is separate\"}\n\nif __name__ == \"__main__\":\n import json; print(json.dumps(main()))"}'

```
{"result":{"msg":"stdout is separate"},"stdout":"print 0\nprint 1\nprint 2\n{\"msg\": \"stdout is separate\"}\n"}
```

## 5. Intentional validation failure — no main() defined
curl -X POST https://safe-py-executor-498806096988.us-central1.run.app/execute \
  -H 'Content-Type: application/json' \
  -d '{"script":"def foo():\n  return 1"}'
```
{"error":"main() must return a valid JSON object"}
```

---

# Completion Details

**Approximate Time Spent**: ~2–2.5 hours


