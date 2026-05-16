from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="OSG-CI™ Layer 1 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Data ──────────────────────────────────────────────────────────────────────

SYSTEM = {
    "name": "OSG-CI™",
    "full_name": "Operational Sovereignty Governance — Competitive Intelligence",
    "layer": "Layer 1B",
    "layer_name": "Constitutional Governance Kernel",
    "system_status": "OPERATIONAL — ALL SERVICES LIVE",
    "tier_achieved": "Tier 2 — Runtime Stabilization",
    "organization": "Olive & Oregano Enterprises",
    "classification": "Internal Engineering Document",
    "build_date": "May 15, 2026",
    "total_containers": 18,
    "total_files": 65,
    "total_directories": 48,
}

HIERARCHY = [
    {"level": "ROOT AUTHORITY", "name": "Human Sovereign", "role": "Priority: 100", "priority": 100},
    {"level": "LAYER 1", "name": "Constitutional Governance Kernel", "role": "Policy Arbiter", "priority": 90},
    {"level": "LAYER 2", "name": "Policy Arbitration Runtime (OPA)", "role": "Rego Rule Engine", "priority": 80},
    {"level": "LAYER 3", "name": "AI Runtime Mesh", "role": "Intelligence Layer", "priority": 70},
    {"level": "LAYER 4", "name": "Operational Services", "role": "Microservice Layer", "priority": 60},
    {"level": "LAYER 5", "name": "Autonomous Intelligence Processes", "role": "RISE Engine", "priority": 50},
]

GOVERNANCE_SERVICES = [
    {"service": "auth-service", "port": 8001, "status": "OPERATIONAL", "function": "JWT issuance/refresh/revoke, RBAC/ABAC, service identity, Keycloak OIDC integration"},
    {"service": "policy-service", "port": 8002, "status": "OPERATIONAL", "function": "OPA governance enforcement, constitutional + operational Rego evaluation, policy logging"},
    {"service": "audit-service", "port": 8003, "status": "OPERATIONAL", "function": "SHA-256 hash-chained immutable event log, ClickHouse analytics, chain integrity verification"},
    {"service": "arbitration-service", "port": 8004, "status": "OPERATIONAL", "function": "Priority-matrix conflict resolution, permission escalation workflow with approve/deny"},
    {"service": "survivability-service", "port": 8005, "status": "OPERATIONAL", "function": "Operational mode FSM (normal→degraded→isolated→recovery→emergency), node quarantine"},
    {"service": "constraint-service", "port": 8006, "status": "OPERATIONAL", "function": "Recursive process registry, propagation depth limits, confidence thresholds, simulation isolation"},
]

INFRASTRUCTURE_SERVICES = [
    {"service": "PostgreSQL 16", "port": 5432, "status": "OPERATIONAL", "function": "Governance/security/audit schemas — users, roles, policies, sessions, constraints, quarantine"},
    {"service": "ClickHouse 23.8", "port": 8123, "status": "OPERATIONAL", "function": "Immutable audit chain analytics, policy evaluation logs, constraint violation history"},
    {"service": "Redis 7", "port": 6379, "status": "OPERATIONAL", "function": "Recursive process registry cache, session tokens, operational state"},
    {"service": "OPA (latest)", "port": 8181, "status": "OPERATIONAL", "function": "Open Policy Agent — evaluates Rego constitutional and operational policies in real-time"},
    {"service": "Keycloak 23", "port": 8180, "status": "OPERATIONAL", "function": "Identity provider — OIDC/OAuth2, MFA, federation, role management"},
    {"service": "Vault 1.15", "port": 8200, "status": "OPERATIONAL", "function": "Secret storage, PKI engine, dynamic credentials, transit encryption"},
    {"service": "Redpanda", "port": 9092, "status": "OPERATIONAL", "function": "Event streaming backbone — Kafka-compatible, sovereign messaging layer"},
    {"service": "MinIO", "port": 9001, "status": "OPERATIONAL", "function": "Long-term audit archive, object storage for immutable event logs"},
]

OBSERVABILITY_SERVICES = [
    {"service": "Grafana", "port": 3000, "status": "OPERATIONAL", "function": "Governance, security, and intelligence dashboards (admin / osg_grafana_secret)"},
    {"service": "Prometheus", "port": 9090, "status": "OPERATIONAL", "function": "Metrics collection across all 6 governance services"},
    {"service": "Loki", "port": 3100, "status": "OPERATIONAL", "function": "Log aggregation — structured logs from all services"},
    {"service": "Jaeger", "port": 16686, "status": "OPERATIONAL", "function": "Distributed tracing — end-to-end request lineage across services"},
]

LIVE_TESTS = [
    {"id": 1, "name": "AI Attempts to Override Human Decision", "result": "DENIED",
     "input": "ai-agent → action: override_human_decision → resource: procurement-order → confidence: 0.99",
     "output": "Constitutional violation: AI systems cannot override human decisions — Human Sovereignty Above AI."},
    {"id": 2, "name": "Human Operator Reads Vendor Catalog", "result": "ALLOWED",
     "input": "commander (human) → action: read → resource: vendor-catalog → confidence: 1.0",
     "output": "No constitutional or operational violations detected. Action permitted."},
    {"id": 3, "name": "Conflict Arbitration: Human vs AI", "result": "HUMAN WINS",
     "input": "commander (root-sovereign, priority 100) vs rise-runtime (ai-operator, priority 70)",
     "output": "commander supersedes rise-runtime. Action: HALT executes. AI propagation blocked."},
    {"id": 4, "name": "Constraint Engine: Low-Confidence Global Propagation", "result": "BLOCKED",
     "input": "rise-ai → action: global_propagation → confidence: 0.55 (below 0.80 threshold)",
     "output": "Confidence 0.55 below minimum 0.80 for action 'global_propagation'. Process terminated."},
    {"id": 5, "name": "Audit Chain: Genesis Block Created", "result": "CHAINED",
     "input": "root-sovereign → event: layer1.boot → service: auth-service",
     "output": "SHA-256 hash: e13b839e4b5d73ac4de983723d6f140e0270070b... Previous: (genesis block). Chain intact."},
    {"id": 6, "name": "Survivability Status", "result": "NORMAL",
     "input": "System mode check → operational_mode",
     "output": "Mode: NORMAL. Transitions: 0. Quarantined nodes: 0. All systems operational."},
]

CONSTITUTIONAL_POLICIES = [
    {"rule": "Autonomous Privilege Escalation", "enforcement": "ALWAYS DENIED", "description": "No AI or service may escalate its own privileges under any condition.", "severity": "critical"},
    {"rule": "Cross-Domain Propagation", "enforcement": "DENIED without auth", "description": "Intelligence cannot cross domain boundaries without explicit human authorization.", "severity": "high"},
    {"rule": "Global Propagation < 80% confidence", "enforcement": "DENIED", "description": "Low-confidence intelligence is constitutionally blocked from system-wide propagation.", "severity": "high"},
    {"rule": "AI Override Human Decision", "enforcement": "ALWAYS DENIED", "description": "AI systems can never override, countermand, or supersede a human decision.", "severity": "critical"},
    {"rule": "Simulation → Production Write", "enforcement": "ALWAYS DENIED", "description": "Simulation environments are constitutionally isolated from production runtimes.", "severity": "critical"},
    {"rule": "Federation Override", "enforcement": "Root-sovereign only", "description": "Only the root-sovereign role may authorize federation-level overrides.", "severity": "high"},
    {"rule": "Governance Bypass", "enforcement": "ALWAYS DENIED", "description": "There is no condition under which governance may be bypassed.", "severity": "critical"},
]

OPERATIONAL_POLICIES = [
    {"condition": "Vendor Risk Score > 0.85", "enforcement": "vendor_approve blocked", "severity": "high"},
    {"condition": "Forecast Confidence < 0.70", "enforcement": "forecast_propagate blocked", "severity": "medium"},
    {"condition": "Data Retention > 7 years", "enforcement": "data_retain blocked", "severity": "medium"},
    {"condition": "audit-observer role", "enforcement": "Read-only — all writes blocked", "severity": "info"},
    {"condition": "Federation sync without key", "enforcement": "federation_sync blocked", "severity": "high"},
    {"condition": "Model validation < 0.75", "enforcement": "model_deploy blocked", "severity": "high"},
]

STABILIZATION_REQUIREMENTS = [
    {"requirement": "Identity Integrity", "status": "COMPLETE", "notes": "auth-service + Keycloak — JWT issuance, RBAC/ABAC, service identity validation"},
    {"requirement": "Policy Enforcement", "status": "COMPLETE", "notes": "policy-service + OPA — constitutional and operational rules active"},
    {"requirement": "Immutable Auditing", "status": "COMPLETE", "notes": "audit-service + ClickHouse — SHA-256 hash-chained event log operational"},
    {"requirement": "Recursive Constraint Enforcement", "status": "COMPLETE", "notes": "constraint-service — propagation limits, confidence thresholds active"},
    {"requirement": "Survivability Controls", "status": "COMPLETE", "notes": "survivability-service — mode FSM, node quarantine, health monitoring"},
    {"requirement": "Permission Arbitration", "status": "COMPLETE", "notes": "arbitration-service — priority matrix, escalation workflow"},
    {"requirement": "Runtime Isolation", "status": "COMPLETE", "notes": "Kubernetes namespace manifests + network policies defined"},
    {"requirement": "Observability Stack", "status": "COMPLETE", "notes": "Prometheus + Grafana + Loki + Jaeger — all operational"},
    {"requirement": "Production Kubernetes Deployment", "status": "PENDING", "notes": "Manifests ready — cluster deployment pending"},
    {"requirement": "Adversarial Stress Testing", "status": "PENDING", "notes": "Layer 3 stabilization — not yet started"},
    {"requirement": "Cryptographic mTLS Validation", "status": "PENDING", "notes": "Certificates defined — runtime validation pending"},
]

STABILIZATION_TIERS = [
    {"tier": "Tier 1", "description": "Conceptual Stabilization — architecture coherent, logic consistent", "status": "COMPLETE"},
    {"tier": "Tier 2", "description": "Runtime Stabilization — services deployed, policies executing, infrastructure live", "status": "COMPLETE"},
    {"tier": "Tier 3", "description": "Adversarial Stabilization — attacks survive, recursive corruption fails", "status": "IN PROGRESS"},
    {"tier": "Tier 4", "description": "Recursive Sovereign Stabilization — intelligence evolves safely under governance", "status": "FUTURE STATE"},
]

TECH_STACK = [
    {"layer": "API Runtime", "technology": "FastAPI + Uvicorn", "version": "0.115 / 0.30", "purpose": "All 6 governance microservices"},
    {"layer": "Identity", "technology": "Keycloak + JWT", "version": "23.0 / HS256", "purpose": "Authentication, RBAC/ABAC, OIDC"},
    {"layer": "Policy Engine", "technology": "Open Policy Agent", "version": "latest", "purpose": "Constitutional + operational rule enforcement"},
    {"layer": "Transactional DB", "technology": "PostgreSQL", "version": "16", "purpose": "Governance, security, audit schemas"},
    {"layer": "Analytics DB", "technology": "ClickHouse", "version": "23.8", "purpose": "Immutable audit chain, policy logs"},
    {"layer": "Cache / Registry", "technology": "Redis", "version": "7", "purpose": "Process registry, session cache"},
    {"layer": "Event Streaming", "technology": "Redpanda", "version": "latest", "purpose": "Kafka-compatible sovereign message bus"},
    {"layer": "Object Storage", "technology": "MinIO", "version": "latest", "purpose": "Long-term audit archive"},
    {"layer": "Secrets", "technology": "HashiCorp Vault", "version": "1.15", "purpose": "PKI, dynamic secrets, encryption"},
    {"layer": "Containers", "technology": "Docker / Compose", "version": "29.4 / v3", "purpose": "Local dev + service orchestration"},
    {"layer": "Orchestration", "technology": "Kubernetes", "version": "manifests", "purpose": "Production namespace isolation"},
    {"layer": "IaC", "technology": "Terraform", "version": "HCL", "purpose": "Reproducible infrastructure provisioning"},
    {"layer": "Metrics", "technology": "Prometheus + Grafana", "version": "latest", "purpose": "System observability"},
    {"layer": "Tracing", "technology": "Jaeger", "version": "latest", "purpose": "Distributed request tracing"},
]

# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"status": "OSG-CI™ Layer 1 API operational", "version": "1.0.0"}

@app.get("/api/system")
def get_system():
    return SYSTEM

@app.get("/api/hierarchy")
def get_hierarchy():
    return HIERARCHY

@app.get("/api/services")
def get_services():
    return {
        "governance": GOVERNANCE_SERVICES,
        "infrastructure": INFRASTRUCTURE_SERVICES,
        "observability": OBSERVABILITY_SERVICES,
        "total": len(GOVERNANCE_SERVICES) + len(INFRASTRUCTURE_SERVICES) + len(OBSERVABILITY_SERVICES),
    }

@app.get("/api/tests")
def get_tests():
    return LIVE_TESTS

@app.get("/api/policies")
def get_policies():
    return {
        "constitutional": CONSTITUTIONAL_POLICIES,
        "operational": OPERATIONAL_POLICIES,
    }

@app.get("/api/stabilization")
def get_stabilization():
    return {
        "requirements": STABILIZATION_REQUIREMENTS,
        "tiers": STABILIZATION_TIERS,
    }

@app.get("/api/tech-stack")
def get_tech_stack():
    return TECH_STACK

@app.get("/api/build")
def get_build():
    return {
        "repository": "C:\\Users\\Flerida\\Documents\\osg-ci",
        "total_files": 65,
        "total_directories": 48,
        "docker_compose": "18-container sovereign runtime stack",
        "governance_services": "6 FastAPI microservices (auth, policy, audit, arbitration, survivability, constraint)",
        "policy_engine": "OPA + 2 Rego policy packages (constitutional + operational)",
        "database_schemas": "PostgreSQL — 3 schemas, 20+ tables (governance, security, audit)",
        "audit_engine": "ClickHouse SHA-256 hash-chained immutable event log",
        "kubernetes": "Namespace manifests + network isolation policies for 6 namespaces",
        "terraform": "Infrastructure modules (kubernetes, networking, security, storage) + dev environment",
        "cicd_pipeline": "GitHub Actions — lint → security scan → OPA validation → build+sign → K8s verify → runtime tests",
        "observability": "Prometheus + Grafana + Loki (logs) + Jaeger (tracing)",
        "identity": "Keycloak 23 — 6 sovereign roles with constitutional priority hierarchy",
        "secrets": "HashiCorp Vault 1.15 — dev mode, PKI engine, dynamic credentials",
        "streaming": "Redpanda (Kafka-compatible) + MinIO object storage",
    }

@app.get("/api/compare")
def get_compare():
    return {
        "constitutional_policies": CONSTITUTIONAL_POLICIES,
        "operational_policies": OPERATIONAL_POLICIES,
        "tiers": STABILIZATION_TIERS,
        "summary": {
            "constitutional_count": len(CONSTITUTIONAL_POLICIES),
            "operational_count": len(OPERATIONAL_POLICIES),
            "always_denied": sum(1 for p in CONSTITUTIONAL_POLICIES if p["enforcement"] == "ALWAYS DENIED"),
            "critical_rules": sum(1 for p in CONSTITUTIONAL_POLICIES if p["severity"] == "critical"),
        },
    }


# ── Layer 2 Data ───────────────────────────────────────────────────────────────

LAYER2_SUBSYSTEMS = [
    {"id": "I",    "name": "Distributed Kubernetes Fabric",       "purpose": "Runtime orchestration"},
    {"id": "II",   "name": "Service Mesh Runtime",                "purpose": "Secure service communication"},
    {"id": "III",  "name": "Persistent Storage Fabric",           "purpose": "Durable intelligence state"},
    {"id": "IV",   "name": "Ingress & Traffic Fabric",            "purpose": "Runtime routing"},
    {"id": "V",    "name": "Distributed Event Fabric",            "purpose": "Intelligence propagation"},
    {"id": "VI",   "name": "Federation Runtime",                  "purpose": "Multi-node synchronization"},
    {"id": "VII",  "name": "Runtime Scaling Engine",              "purpose": "Adaptive elasticity"},
    {"id": "VIII", "name": "Synchronization Infrastructure",      "purpose": "Recursive intelligence consistency"},
    {"id": "IX",   "name": "Sovereign Networking Layer",          "purpose": "Operational isolation"},
    {"id": "X",    "name": "Infrastructure Observability",        "purpose": "Runtime visibility"},
    {"id": "XI",   "name": "Chaos & Survivability Engineering",   "purpose": "Enterprise resilience"},
]

LAYER2_KUBERNETES = [
    {"num": 1, "name": "Governance Cluster",    "handles": ["policy enforcement", "identity", "constitutional runtime", "survivability controls"]},
    {"num": 2, "name": "Intelligence Cluster",  "handles": ["invoice intelligence", "procurement intelligence", "anomaly detection", "AI inference"]},
    {"num": 3, "name": "Forecasting Cluster",   "handles": ["ACIFR", "economic forecasting", "commodity prediction", "causal inference"]},
    {"num": 4, "name": "Federation Cluster",    "handles": ["regional synchronization", "distributed intelligence replication", "node coordination"]},
]

LAYER2_SERVICE_MESH = [
    {"function": "Service Mesh",      "technology": "Istio"},
    {"function": "Runtime Encryption","technology": "mTLS"},
    {"function": "Traffic Control",   "technology": "Envoy"},
    {"function": "Service Identity",  "technology": "SPIFFE/SPIRE"},
]

LAYER2_STORAGE = [
    {"type": "Relational",        "technology": "PostgreSQL",   "purpose": "Governance, security, and audit schemas"},
    {"type": "Time-Series",       "technology": "TimescaleDB",  "purpose": "Temporal intelligence patterns and forecasting data"},
    {"type": "Cache",             "technology": "Redis",        "purpose": "Process registry, session tokens, operational state"},
    {"type": "Analytics",         "technology": "ClickHouse",   "purpose": "Immutable audit chain analytics, policy evaluation logs"},
    {"type": "Graph Intelligence","technology": "Neo4j",        "purpose": "Causal correlation, entity relationships, intelligence graphs"},
    {"type": "Vector Memory",     "technology": "Qdrant",       "purpose": "AI embedding storage, semantic search, intelligence retrieval"},
    {"type": "Object Storage",    "technology": "MinIO",        "purpose": "Invoices, audit archives, forecasting models, simulation outputs"},
]

LAYER2_EVENT_TOPICS = [
    "invoice.parsed", "vendor.anomaly", "forecast.generated", "institutional.shift",
    "commodity.volatility", "logistics.delay", "recursive.sync", "policy.violation",
]

LAYER2_EVENT_STACK = [
    {"function": "Event Streaming", "technology": "Redpanda"},
    {"function": "Messaging",       "technology": "NATS"},
    {"function": "Workflow Runtime","technology": "Temporal"},
    {"function": "Event Replay",    "technology": "Kafka-compatible retention"},
]

LAYER2_FEDERATION_NODES = ["Regional Node A", "Regional Node B", "Regional Node C"]

LAYER2_SCALING_STACK = [
    {"function": "Autoscaling",    "technology": "KEDA"},
    {"function": "Cluster Scaling","technology": "Cluster Autoscaler"},
    {"function": "Load Metrics",   "technology": "Prometheus"},
    {"function": "Event Scaling",  "technology": "Kafka lag metrics"},
]

LAYER2_NETWORK_SEGMENTS = [
    {"segment": "Governance Network",    "purpose": "constitutional services"},
    {"segment": "Intelligence Network",  "purpose": "AI runtime"},
    {"segment": "Federation Network",    "purpose": "node synchronization"},
    {"segment": "Observability Network", "purpose": "monitoring"},
    {"segment": "Public Edge",           "purpose": "ingress only"},
]

LAYER2_OBSERVABILITY = [
    {"component": "Prometheus",     "purpose": "metrics"},
    {"component": "Grafana",        "purpose": "visualization"},
    {"component": "Loki",           "purpose": "logs"},
    {"component": "Jaeger",         "purpose": "tracing"},
    {"component": "OpenTelemetry",  "purpose": "distributed telemetry"},
]

LAYER2_CHAOS_TESTS = [
    "cluster failure", "broker failure", "node partition",
    "service corruption", "storage loss", "federation isolation",
]

LAYER2_SYNC_LOGIC = ["Acquire Intelligence", "Normalize", "Correlate", "Forecast", "Synchronize", "Propagate", "Adapt"]

LAYER2_FINAL_CAPABILITIES = [
    "recursive synchronization", "distributed orchestration",
    "multi-node intelligence federation", "enterprise-scale forecasting",
    "sovereign runtime survivability", "adaptive operational scaling",
]

# ── Layer 2 Routes ─────────────────────────────────────────────────────────────

@app.get("/api/layer2/overview")
def get_layer2_overview():
    return {
        "layer": "Layer 2",
        "name": "Infrastructure Runtime Fabric (IRF)",
        "status": "INITIATING",
        "subsystem_count": len(LAYER2_SUBSYSTEMS),
        "builds_on": "Layer 1B — Constitutional Governance Kernel",
        "subsystems": LAYER2_SUBSYSTEMS,
    }

@app.get("/api/layer2/kubernetes")
def get_layer2_kubernetes():
    return {"clusters": LAYER2_KUBERNETES, "count": len(LAYER2_KUBERNETES)}

@app.get("/api/layer2/storage")
def get_layer2_storage():
    return {"engines": LAYER2_STORAGE, "count": len(LAYER2_STORAGE)}

@app.get("/api/layer2/events")
def get_layer2_events():
    return {
        "stack": LAYER2_EVENT_STACK,
        "topics": LAYER2_EVENT_TOPICS,
        "topology": ["Invoice Event", "Normalization Event", "Causal Correlation Event", "Forecast Event", "RISE Synchronization Event", "Operational Recommendation Event"],
    }

@app.get("/api/layer2/federation")
def get_layer2_federation():
    return {
        "nodes": LAYER2_FEDERATION_NODES,
        "model": "Each node: retains local sovereignty, synchronizes approved intelligence, obeys constitutional federation policy",
    }

@app.get("/api/layer2/scaling")
def get_layer2_scaling():
    return {"stack": LAYER2_SCALING_STACK, "conditions": ["event backlog", "synchronization pressure", "forecasting demand", "AI inference load", "anomaly density"]}

@app.get("/api/layer2/networking")
def get_layer2_networking():
    return {"segments": LAYER2_NETWORK_SEGMENTS, "security": ["Zero Trust Networking", "Runtime Isolation", "Federation Encryption"]}

@app.get("/api/layer2/observability")
def get_layer2_observability():
    return {"stack": LAYER2_OBSERVABILITY, "metrics": ["synchronization latency", "federation drift", "recursive propagation rate", "AI inference latency", "event throughput", "storage pressure", "runtime anomalies"]}

@app.get("/api/layer2/chaos")
def get_layer2_chaos():
    return {"tests": LAYER2_CHAOS_TESTS, "target": ["continue operating", "synchronize safely", "preserve governance", "maintain survivability"]}

@app.get("/api/layer2/sync")
def get_layer2_sync():
    return {"stack": [{"function": f, "technology": t} for f, t in [("Event Coordination","Redpanda"),("Workflow Orchestration","Temporal"),("State Synchronization","Redis"),("Graph Correlation","Neo4j")]], "logic": LAYER2_SYNC_LOGIC}

@app.get("/api/layer2/service-mesh")
def get_layer2_service_mesh():
    return {"stack": LAYER2_SERVICE_MESH, "topology": ["Ingress Gateway", "Envoy Sidecars", "Service-to-Service mTLS", "Policy Enforcement"]}

@app.get("/api/layer2/final-state")
def get_layer2_final_state():
    return {"capabilities": LAYER2_FINAL_CAPABILITIES, "description": "A distributed sovereign intelligence infrastructure fabric — the system transitions from governance infrastructure into a true enterprise intelligence nervous system."}

@app.get("/api/layer2")
def get_layer2_all():
    return {
        "overview": {"layer": "Layer 2", "name": "Infrastructure Runtime Fabric (IRF)", "status": "INITIATING", "subsystems": LAYER2_SUBSYSTEMS},
        "kubernetes": {"clusters": LAYER2_KUBERNETES},
        "service_mesh": {"stack": LAYER2_SERVICE_MESH},
        "storage": {"engines": LAYER2_STORAGE},
        "events": {"stack": LAYER2_EVENT_STACK, "topics": LAYER2_EVENT_TOPICS},
        "federation": {"nodes": LAYER2_FEDERATION_NODES},
        "scaling": {"stack": LAYER2_SCALING_STACK},
        "networking": {"segments": LAYER2_NETWORK_SEGMENTS},
        "observability": {"stack": LAYER2_OBSERVABILITY},
        "chaos": {"tests": LAYER2_CHAOS_TESTS},
        "sync": {"logic": LAYER2_SYNC_LOGIC},
        "final_capabilities": LAYER2_FINAL_CAPABILITIES,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
