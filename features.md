# 🚀 RootLens — Development Roadmap

## 🎯 Goal

Build a system that ingests logs, correlates events, and identifies root causes of failures with structured insights.

# 📥 Phase 1: Log Ingestion (FOUNDATION)

## Step 1.1 — Log Schema Design

* Define log structure:

  * timestamp
  * service
  * level
  * message
  * trace_id

## Step 1.2 — DB Model

* Create Log table
* Add indexes (timestamp, service, trace_id)

## Step 1.3 — Ingestion API

* Endpoint: `POST /ingest-log`
* Validate input (Pydantic)
* Store logs in DB

## Step 1.4 — Bulk Ingestion (Optional but useful)

* Endpoint: `POST /ingest-logs`
* Accept list of logs

---

# 🔍 Phase 2: Log Query System

## Step 2.1 — Fetch Logs

* Endpoint: `GET /logs`
* Filters:

  * time range
  * service
  * level

## Step 2.2 — Pagination

* Add limit + offset
* Prevent heavy queries

## Step 2.3 — Basic UI (Frontend Start)

* Display logs table
* Filters UI

---

# 🔗 Phase 3: Event Correlation

## Step 3.1 — Correlation Logic (v1)

* Group logs by:

  * same `trace_id`
  * time window (±5 sec)

## Step 3.2 — Pattern Matching

* Cluster similar error messages
* Example:

  * "DB timeout"
  * "DB connection failed"

## Step 3.3 — Correlation API

* Endpoint: `GET /correlate`
* Input: time range / incident window
* Output: grouped events

---

# 🕒 Phase 4: Timeline Reconstruction (CRITICAL)

## Step 4.1 — Sort Events

* Order logs by timestamp

## Step 4.2 — Build Timeline

* Extract key events
* Remove noise logs

## Step 4.3 — Timeline API

* Endpoint: `GET /timeline`
* Output:

  * ordered sequence of failures

## Step 4.4 — Frontend Visualization

* Timeline UI component
* Clean readable format

---

# 🧠 Phase 5: Root Cause Analysis

## Step 5.1 — Rule-Based Detection (MANDATORY FIRST)

* Identify:

  * first error spike
  * most frequent error
  * service causing failure

## Step 5.2 — AI Explanation Layer

* Send clustered logs to LLM
* Generate explanation

## Step 5.3 — Root Cause API

* Endpoint: `POST /analyze`
* Output:

  * root cause
  * reasoning

---

# 📊 Phase 6: Impact Analysis

## Step 6.1 — Service Impact

* Count affected services

## Step 6.2 — Severity Score

* Based on:

  * error volume
  * number of services
  * duration

## Step 6.3 — Duration Calculation

* First error → last error

---

# 📦 Phase 7: Incident Summary (PRODUCT FEATURE)

## Step 7.1 — Combine Outputs

* Root cause
* Timeline
* Impact

## Step 7.2 — Final API

* Endpoint: `GET /incident-summary`

## Step 7.3 — Frontend Dashboard

* Show:

  * summary card
  * timeline
  * affected services

---

# ⚙️ Phase 8: Async Processing (Upgrade)

## Step 8.1 — Add Redis

* Setup queue system

## Step 8.2 — Background Workers

* Move analysis to async jobs

## Step 8.3 — Job Status Tracking

* Track analysis progress

---

# 🧪 Phase 9: Data Simulation (IMPORTANT)

## Step 9.1 — Log Generator Script

* Simulate:

  * DB failures
  * API failures
  * cascading failures

## Step 9.2 — Test Scenarios

* Single service failure
* Multi-service cascade
* gradual degradation

---

# 🐳 Phase 10: Dockerization

## Step 10.1 — Backend Container

## Step 10.2 — Database Container

## Step 10.3 — docker-compose setup

---

# 🎯 Phase 11: Advanced Features (ONLY AFTER MVP)

## Feature 1 — Anomaly Detection

* Detect unusual patterns

## Feature 2 — Deployment Correlation

* Link failures with releases

## Feature 3 — Alert System

* Notify on critical incidents

## Feature 4 — Visualization Improvements

* graphs, heatmaps

---

# ⚠️ Rules You Must Follow

* Build **feature by feature**, not everything at once
* Never jump to AI before rule-based logic works
* Always test with real-like data
* Backend > frontend (priority)

---

# 🧠 Final Execution Order (STRICT)

1. Setup backend
2. Log ingestion
3. Log querying
4. Correlation
5. Timeline
6. Root cause
7. Impact
8. Summary
9. Frontend
10. Infra

---

# 💣 Reality Check

If you stop at:

* ingestion + logs → beginner project
* add correlation → intermediate
* add root cause + timeline → **this becomes elite**

---

# 🚀 Definition of Done (MVP)

You can input logs and get:

* clear failure timeline
* identified root cause
* impact summary

If you reach this → your project is legit.
