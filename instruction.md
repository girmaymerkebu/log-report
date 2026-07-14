An Apache-style access log is located at `/app/access.log`. Each line has the form:

    <client_ip> - - [<timestamp>] "<METHOD> <path> HTTP/1.1" <status> <bytes>

Write a JSON summary report to `/app/report.json`.

Success criteria:

1. The file `/app/report.json` exists and contains a single valid JSON object.
2. The object has exactly these three keys and no others:
   - `total_requests` (integer): the number of non-empty lines in `/app/access.log`.
   - `unique_ips` (integer): the number of distinct client IP addresses (the first
     whitespace-separated field of each line).
   - `top_path` (string): the request path that appears most often in the request
     line (the path is the second token inside the quoted request, e.g.
     `/index.html`). The log is guaranteed to have a unique most-frequent path.
