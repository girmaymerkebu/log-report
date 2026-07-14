An Apache-style access log is located at `/app/access.log`. Each line has the form:

    <client_ip> - - [<timestamp>] "<METHOD> <path> HTTP/1.1" <status> <bytes>

Analyze the log and write a JSON summary report to `/app/report.json`.

Success criteria:

1. The file `/app/report.json` exists and contains a single valid JSON object.
2. The object has exactly these three keys and no others: `total_requests`,
   `unique_ips`, `top_path`.
3. `total_requests` is an integer equal to the number of non-empty lines in
   `/app/access.log`.
4. `unique_ips` is an integer equal to the number of distinct client IP
   addresses (the first whitespace-separated field of each line).
5. `top_path` is a string equal to the request path that appears most often
   (the path is the second token inside the quoted request line, e.g.
   `/index.html`). The log is guaranteed to have a unique most-frequent path.
