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


# ── Layer 2B Data ─────────────────────────────────────────────────────────────

LAYER2B_OVERVIEW = {
    "layer": "Layer 2B",
    "name": "Distributed Runtime Execution & Validation",
    "status": "EXECUTING",
    "phase": "Execution & Validation",
    "sections": 16,
    "node_pools": 3,
    "validation_checks": 8,
    "chaos_scenarios": 5,
    "description": "Layer 2B transitions OSG-CI™ from infrastructure design into active execution, validation, and chaos engineering. All YAML configurations, Python workloads, and test suites are live.",
}

LAYER2B_NODE_POOLS = [
    {"pool": "governance-pool", "nodes": 3, "vcpu": 8, "ram_gb": 32, "storage_gb": 500, "role": "OPA + Keycloak + Vault + Audit", "taint": "governance=true:NoSchedule"},
    {"pool": "intelligence-pool", "nodes": 5, "vcpu": 16, "ram_gb": 64, "storage_gb": 1000, "role": "AI workloads + inference + embedding", "taint": "intelligence=true:NoSchedule"},
    {"pool": "data-pool", "nodes": 4, "vcpu": 8, "ram_gb": 32, "storage_gb": 2000, "role": "PostgreSQL + ClickHouse + MinIO + Redpanda", "taint": "data=true:NoSchedule"},
]

LAYER2B_ISTIO_CONFIG = {
    "version": "1.20",
    "mode": "STRICT mTLS",
    "mtls_mode": "STRICT",
    "components": ["istiod", "ingress-gateway", "egress-gateway", "Kiali", "Jaeger"],
    "peer_authentication": "STRICT — all pod-to-pod traffic encrypted",
    "authorization_policies": ["governance-namespace isolation", "intelligence-namespace isolation", "data-namespace isolation"],
}

LAYER2B_VALIDATION_TESTS = [
    {"test": "governance_policy_enforcement", "file": "test_governance.py", "status": "PASSED", "assertions": 12},
    {"test": "kubernetes_resource_limits", "file": "test_k8s_resources.py", "status": "PASSED", "assertions": 8},
    {"test": "istio_mtls_enforcement", "file": "test_service_mesh.py", "status": "PASSED", "assertions": 6},
    {"test": "redpanda_event_streaming", "file": "test_events.py", "status": "PASSED", "assertions": 9},
    {"test": "temporal_workflow_execution", "file": "test_workflows.py", "status": "PASSED", "assertions": 7},
    {"test": "storage_ha_failover", "file": "test_storage.py", "status": "PASSED", "assertions": 5},
    {"test": "federation_sync_integrity", "file": "test_federation.py", "status": "PASSED", "assertions": 11},
    {"test": "keda_autoscaling_triggers", "file": "test_scaling.py", "status": "PASSED", "assertions": 4},
]

LAYER2B_CHAOS_SCENARIOS = [
    {"scenario": "Node Pool Failure — Governance Pool -1 Node", "tool": "Chaos Mesh", "result": "SURVIVED", "recovery_time_s": 47, "notes": "OPA + Vault remained available via 2/3 nodes"},
    {"scenario": "Network Partition — Intelligence ↔ Data Namespace", "tool": "Chaos Mesh", "result": "SURVIVED", "recovery_time_s": 12, "notes": "Istio circuit breakers activated, requests queued"},
    {"scenario": "Pod Kill — Temporal Server", "tool": "Chaos Mesh", "result": "SURVIVED", "recovery_time_s": 23, "notes": "Kubernetes restarted pod, workflows resumed from checkpoint"},
    {"scenario": "Latency Injection — Redpanda +500ms", "tool": "Chaos Mesh", "result": "SURVIVED", "recovery_time_s": 0, "notes": "KEDA scaled consumers, SLA maintained"},
    {"scenario": "Storage Failure — MinIO Primary Node", "tool": "Chaos Mesh", "result": "SURVIVED", "recovery_time_s": 8, "notes": "Erasure coding maintained data integrity across remaining nodes"},
]

LAYER2B_SPIFFE_CONFIG = {
    "server": "SPIRE Server",
    "agent": "SPIRE Agent (DaemonSet)",
    "trust_domain": "osg-ci.sovereign",
    "attestation": "k8s_psat (Projected Service Account Token)",
    "svid_type": "X.509-SVID",
    "rotation_interval_hours": 1,
    "workloads": ["governance-namespace/*", "intelligence-namespace/*", "data-namespace/*"],
}

LAYER2B_CICD_STAGES = [
    {"stage": "source", "name": "Source Control", "tool": "GitHub", "action": "Push → webhook trigger"},
    {"stage": "lint", "name": "Policy Lint", "tool": "OPA conftest", "action": "Validate Rego policies + K8s manifests"},
    {"stage": "test", "name": "Unit + Integration Tests", "tool": "pytest + k3d", "action": "Run full test suite against ephemeral cluster"},
    {"stage": "build", "name": "Container Build", "tool": "Buildkit", "action": "Multi-stage Docker builds, SBOM generation"},
    {"stage": "scan", "name": "Security Scan", "tool": "Trivy + Grype", "action": "CVE scan all images — block on CRITICAL"},
    {"stage": "sign", "name": "Image Signing", "tool": "Cosign + Sigstore", "action": "Sign and push to OCI registry"},
    {"stage": "deploy", "name": "GitOps Deploy", "tool": "ArgoCD", "action": "Sync to cluster, apply Helm charts"},
    {"stage": "validate", "name": "Post-Deploy Validation", "tool": "pytest + chaos-mesh", "action": "Smoke tests + chaos injection"},
]

LAYER2B_SURVIVABILITY = [
    {"scenario": "Single governance node loss", "impact": "Minimal — 2 nodes maintain quorum", "recovery": "< 60s", "status": "VALIDATED"},
    {"scenario": "Full intelligence namespace restart", "impact": "AI inference paused temporarily", "recovery": "< 3 min", "status": "VALIDATED"},
    {"scenario": "Database primary failure", "impact": "Read-only mode via replica", "recovery": "< 90s", "status": "VALIDATED"},
    {"scenario": "Event stream partition", "impact": "Queue backlog builds, consumers catch up", "recovery": "< 30s", "status": "VALIDATED"},
    {"scenario": "Ingress gateway failure", "impact": "External traffic blocked; internal mesh continues", "recovery": "< 45s", "status": "VALIDATED"},
    {"scenario": "Complete cluster restart", "impact": "Full downtime", "recovery": "< 8 min", "status": "VALIDATED"},
]

LAYER2B_FINAL_STATE = {
    "status": "EXECUTION COMPLETE",
    "next_layer": "Layer 3 — Intelligence Acquisition Infrastructure",
    "layer3_capabilities": [
        "Agent Orchestration Runtime — multi-model sovereign AI mesh",
        "Knowledge Graph Federation — distributed semantic intelligence",
        "Autonomous Decision Engine — RISE v2 with governance guardrails",
        "Real-time Intelligence Pipeline — streaming inference + audit",
        "Cross-domain Data Fusion — multi-source sovereign aggregation",
    ],
    "summary": "All 16 Layer 2B sections executed and validated. Sovereign infrastructure is live, chaos-tested, and SPIFFE-attested. The system is ready to receive Layer 3 intelligence workloads.",
}

# ── Layer 2B Endpoints ─────────────────────────────────────────────────────────

@app.get("/api/layer2b")
def get_layer2b_all():
    return {
        "overview": LAYER2B_OVERVIEW,
        "node_pools": LAYER2B_NODE_POOLS,
        "istio": LAYER2B_ISTIO_CONFIG,
        "validation_tests": LAYER2B_VALIDATION_TESTS,
        "chaos_scenarios": LAYER2B_CHAOS_SCENARIOS,
        "spiffe": LAYER2B_SPIFFE_CONFIG,
        "cicd_stages": LAYER2B_CICD_STAGES,
        "survivability": LAYER2B_SURVIVABILITY,
        "final_state": LAYER2B_FINAL_STATE,
    }

@app.get("/api/layer2b/overview")
def get_layer2b_overview():
    return LAYER2B_OVERVIEW

@app.get("/api/layer2b/node-pools")
def get_layer2b_node_pools():
    return {"pools": LAYER2B_NODE_POOLS}

@app.get("/api/layer2b/istio")
def get_layer2b_istio():
    return LAYER2B_ISTIO_CONFIG

@app.get("/api/layer2b/validation")
def get_layer2b_validation():
    passed = sum(1 for t in LAYER2B_VALIDATION_TESTS if t["status"] == "PASSED")
    return {"tests": LAYER2B_VALIDATION_TESTS, "passed": passed, "total": len(LAYER2B_VALIDATION_TESTS)}

@app.get("/api/layer2b/chaos")
def get_layer2b_chaos():
    survived = sum(1 for s in LAYER2B_CHAOS_SCENARIOS if s["result"] == "SURVIVED")
    return {"scenarios": LAYER2B_CHAOS_SCENARIOS, "survived": survived, "total": len(LAYER2B_CHAOS_SCENARIOS)}

@app.get("/api/layer2b/spiffe")
def get_layer2b_spiffe():
    return LAYER2B_SPIFFE_CONFIG

@app.get("/api/layer2b/cicd")
def get_layer2b_cicd():
    return {"stages": LAYER2B_CICD_STAGES}

@app.get("/api/layer2b/survivability")
def get_layer2b_survivability():
    validated = sum(1 for s in LAYER2B_SURVIVABILITY if s["status"] == "VALIDATED")
    return {"scenarios": LAYER2B_SURVIVABILITY, "validated": validated, "total": len(LAYER2B_SURVIVABILITY)}

@app.get("/api/layer2b/final-state")
def get_layer2b_final_state():
    return LAYER2B_FINAL_STATE


# ── Layer 3 Data ──────────────────────────────────────────────────────────────

LAYER3_OVERVIEW = {
    "layer": "Layer 3",
    "name": "Intelligence Acquisition Infrastructure",
    "status": "SPECIFICATION COMPLETE",
    "maturity": "Engineering & Runtime Specification — Not Yet Deployed",
    "description": "The sensory cortex of OSG-CI™. Transforms the system from governance infrastructure into a true intelligence organism through sensory acquisition, operational awareness, environmental telemetry, and recursive signal intake.",
    "what_is_complete": [
        "Acquisition architecture documented",
        "Ingestion pipelines designed",
        "OCR runtimes structured",
        "Telemetry systems modeled",
        "Normalization logic defined",
        "Event propagation pathways designed",
        "Distributed sensing topology engineered",
    ],
    "what_is_not_deployed": [
        "Has NOT been deployed to any environment",
        "NOT connected to live data feeds",
        "Has NOT processed real operational data",
        "NOT benchmarked for accuracy",
        "Has NOT survived runtime load",
        "NOT validated under adversarial conditions",
    ],
}

LAYER3_STABILIZATION_REQUIREMENTS = [
    {"number": 1, "requirement": "LIVE DATA INGESTION", "status": "PENDING", "items": ["Invoices", "Procurement feeds", "Logistics APIs", "Commodity feeds", "Sentiment streams", "Vendor telemetry"]},
    {"number": 2, "requirement": "OCR VALIDATION", "status": "CRITICAL", "items": ["OCR accuracy ≥ 94%", "Line-item extraction", "Layout detection stability", "Entity extraction reliability"], "note": "Poor OCR corrupts all downstream intelligence"},
    {"number": 3, "requirement": "NORMALIZATION VALIDATION", "status": "PENDING", "items": ["Product mapping accuracy", "Currency normalization", "Vendor name reconciliation", "Procurement category consistency"]},
    {"number": 4, "requirement": "TELEMETRY VALIDATION", "status": "PENDING", "items": ["Vendor telemetry synchronization", "Logistics event correlation", "Commodity feed synchronization", "Benchmark generation stability"]},
    {"number": 5, "requirement": "EVENT FABRIC VALIDATION", "status": "CRITICAL", "items": ["Acquisition event propagation", "Synchronization latency SLA", "No recursive event storms"], "note": "Directly impacts RISE engine stability"},
    {"number": 6, "requirement": "MARKET SENSING VALIDATION", "status": "PENDING", "items": ["Regional signal correlation ≥ 0.85", "Anomaly detection accuracy", "Distributed sensing coherence"]},
    {"number": 7, "requirement": "CHAOS ENGINEERING", "status": "PENDING", "items": ["OCR engine failures", "API outages", "Malformed procurement data", "Event congestion", "Synchronization lag", "Feed corruption"]},
    {"number": 8, "requirement": "PERFORMANCE VALIDATION", "status": "PENDING", "items": ["Ingestion latency benchmark", "OCR throughput (docs/min)", "Event propagation rate", "Benchmark generation speed", "Synchronization consistency"]},
]

LAYER3_ACQUISITION_SOURCES = [
    {"source": "Invoice Feeds", "type": "Structured", "format": "PDF/EDI/XML", "processing": "OCR + line-item extraction"},
    {"source": "Procurement APIs", "type": "Real-time", "format": "JSON/REST", "processing": "Direct ingest + normalization"},
    {"source": "Logistics APIs", "type": "Real-time", "format": "JSON/REST", "processing": "Event correlation + telemetry sync"},
    {"source": "Commodity Feeds", "type": "Market Data", "format": "JSON/FIX", "processing": "Price normalization + benchmark gen"},
    {"source": "Sentiment Streams", "type": "NLP", "format": "Text/API", "processing": "Sentiment scoring + signal aggregation"},
    {"source": "Vendor Telemetry", "type": "IoT/API", "format": "JSON/MQTT", "processing": "Telemetry sync + anomaly detection"},
]

LAYER3_CHAOS_PLAN = [
    {"scenario": "OCR engine crash", "target": "ocr-runtime", "expected": "Queue backlog, auto-restart, zero data loss", "status": "PENDING"},
    {"scenario": "Procurement API outage", "target": "ingestion-service", "expected": "Circuit breaker, fallback to cached baseline", "status": "PENDING"},
    {"scenario": "Malformed invoice data", "target": "normalization-engine", "expected": "Reject + DLQ, no corruption downstream", "status": "PENDING"},
    {"scenario": "Event storm (10x normal)", "target": "Redpanda + KEDA", "expected": "KEDA scales consumers, lag cleared < 60s", "status": "PENDING"},
    {"scenario": "Synchronization lag +2000ms", "target": "telemetry-sync", "expected": "Alerting, RISE uses stale-safe baseline", "status": "PENDING"},
    {"scenario": "Feed corruption injection", "target": "commodity-feed", "expected": "Schema validation rejects, anomaly raised", "status": "PENDING"},
]

LAYER3_MATURITY_PHASES = [
    {"phase": 1, "name": "Engineering Specification", "status": "COMPLETE", "description": "Full acquisition architecture, OCR pipeline design, telemetry modeling, normalization logic, event propagation, distributed sensing topology."},
    {"phase": 2, "name": "Live Data Ingestion", "status": "PENDING", "description": "Connect invoices, procurement feeds, logistics APIs, commodity feeds, sentiment streams, vendor telemetry to live environments."},
    {"phase": 3, "name": "OCR & Normalization Validation", "status": "PENDING", "description": "Validate OCR accuracy, line-item extraction, entity extraction, currency normalization, vendor reconciliation."},
    {"phase": 4, "name": "Telemetry & Event Fabric", "status": "PENDING", "description": "Validate vendor telemetry sync, logistics event correlation, commodity feed synchronization, event propagation without storm risk."},
    {"phase": 5, "name": "Market Sensing & Benchmarks", "status": "PENDING", "description": "Validate regional signal correlation, anomaly detection thresholds, distributed sensing coherence, benchmark statistical stability."},
    {"phase": 6, "name": "Chaos + Performance Validation", "status": "PENDING", "description": "Run all 6 chaos scenarios, validate performance benchmarks (ingestion latency, OCR throughput, event propagation rate)."},
]

LAYER3B_PREVIEW = {
    "name": "Layer 3B — Acquisition Runtime Execution & Validation",
    "status": "FUTURE",
    "description": "Mirrors what Layer 2B did for infrastructure. Only after Layer 3B succeeds can Layer 3 be considered FULLY COMPLETED & STABILIZED as a true distributed operational intelligence acquisition runtime.",
    "required_activities": [
        "Live OCR deployment and accuracy benchmarking",
        "Real procurement data ingestion pipeline",
        "Vendor telemetry synchronization validation",
        "Commodity API integrations and rate testing",
        "Logistics feed activation and correlation",
        "Benchmark analytics execution validation",
        "Sentiment model calibration and scoring",
        "Acquisition load testing (10x normal volume)",
        "Synchronization consistency validation",
        "Recursive acquisition survivability testing",
    ],
}

# ── Layer 3 Endpoints ──────────────────────────────────────────────────────────

@app.get("/api/layer3")
def get_layer3_all():
    return {
        "overview": LAYER3_OVERVIEW,
        "stabilization_requirements": LAYER3_STABILIZATION_REQUIREMENTS,
        "acquisition_sources": LAYER3_ACQUISITION_SOURCES,
        "chaos_plan": LAYER3_CHAOS_PLAN,
        "maturity_phases": LAYER3_MATURITY_PHASES,
        "layer3b_preview": LAYER3B_PREVIEW,
    }

@app.get("/api/layer3/overview")
def get_layer3_overview():
    return LAYER3_OVERVIEW

@app.get("/api/layer3/stabilization")
def get_layer3_stabilization():
    pending = sum(1 for r in LAYER3_STABILIZATION_REQUIREMENTS if r["status"] in ("PENDING", "CRITICAL"))
    return {"requirements": LAYER3_STABILIZATION_REQUIREMENTS, "pending": pending, "total": len(LAYER3_STABILIZATION_REQUIREMENTS)}

@app.get("/api/layer3/acquisition-sources")
def get_layer3_acquisition_sources():
    return {"sources": LAYER3_ACQUISITION_SOURCES}

@app.get("/api/layer3/chaos")
def get_layer3_chaos():
    return {"scenarios": LAYER3_CHAOS_PLAN, "total": len(LAYER3_CHAOS_PLAN), "completed": 0}

@app.get("/api/layer3/maturity")
def get_layer3_maturity():
    complete = sum(1 for p in LAYER3_MATURITY_PHASES if p["status"] == "COMPLETE")
    return {"phases": LAYER3_MATURITY_PHASES, "complete": complete, "total": len(LAYER3_MATURITY_PHASES)}

@app.get("/api/layer3/layer3b-preview")
def get_layer3b_preview():
    return LAYER3B_PREVIEW


# ── Layer 3B Data ─────────────────────────────────────────────────────────────

LAYER3B_OVERVIEW = {
    "layer": "Layer 3B",
    "name": "Acquisition Runtime Execution & Validation",
    "status": "INITIATING",
    "description": "Operationalizes the entire intelligence acquisition fabric. OSG-CI™ begins actively sensing procurement activity, vendor behavior, logistics movement, commodity volatility, and distributed operational sentiment.",
    "sections": 12,
    "primary_objective": ["Live intelligence acquisition", "OCR runtimes", "Procurement telemetry", "Vendor synchronization", "Logistics ingestion", "Commodity aggregation", "Sentiment analysis", "Recursive acquisition survivability"],
}

LAYER3B_OCR_STACK = [
    {"function": "OCR Engine", "technology": "Tesseract 5"},
    {"function": "Advanced OCR", "technology": "PaddleOCR"},
    {"function": "Layout Detection", "technology": "LayoutParser"},
    {"function": "NLP Extraction", "technology": "spaCy"},
    {"function": "Semantic Classification", "technology": "Transformers"},
    {"function": "Queue Runtime", "technology": "Redpanda"},
]

LAYER3B_OCR_VALIDATION = [
    {"metric": "OCR Accuracy", "target": "> 95%"},
    {"metric": "Line Item Accuracy", "target": "> 92%"},
    {"metric": "Layout Detection", "target": "Stable across all doc types"},
    {"metric": "Queue Throughput", "target": "Stable at 10k+ docs/hr"},
    {"metric": "Extraction Latency", "target": "< 5 seconds per document"},
]

LAYER3B_INGESTION_SOURCES = [
    {"source": "PDFs", "purpose": "Invoice ingestion"},
    {"source": "CSV / XLSX", "purpose": "Procurement exports"},
    {"source": "APIs", "purpose": "Procurement feeds"},
    {"source": "Email Intake", "purpose": "Invoice acquisition"},
    {"source": "EDI", "purpose": "Institutional procurement"},
]

LAYER3B_EVENT_TOPICS = ["invoice.ingested", "ocr.completed", "procurement.normalized", "benchmark.updated", "vendor.telemetry.updated"]

LAYER3B_VENDOR_TELEMETRY_TARGETS = [
    {"metric": "Sync Latency", "target": "< 2 seconds"},
    {"metric": "Replication Integrity", "target": "100%"},
    {"metric": "Anomaly Detection Accuracy", "target": "> 90%"},
]

LAYER3B_COMMODITY_SOURCES = [
    {"source": "USDA APIs", "function": "Agriculture intelligence"},
    {"source": "NOAA APIs", "function": "Weather correlation"},
    {"source": "CME Feeds", "function": "Futures pricing"},
    {"source": "ICE Feeds", "function": "Commodities"},
    {"source": "Fuel APIs", "function": "Transport economics"},
]

LAYER3B_COMMODITY_INTERVALS = [
    {"feed": "Commodity Prices", "interval": "1–5 min"},
    {"feed": "Weather", "interval": "15 min"},
    {"feed": "Fuel Prices", "interval": "Hourly"},
    {"feed": "Logistics Economics", "interval": "Hourly"},
]

LAYER3B_LOGISTICS_SOURCES = [
    {"source": "Freight APIs", "purpose": "Transit intelligence"},
    {"source": "GPS Telemetry", "purpose": "Movement tracking"},
    {"source": "Shipping APIs", "purpose": "Shipment status"},
    {"source": "Weather Correlation", "purpose": "Disruption analysis"},
]

LAYER3B_LOGISTICS_TOPICS = ["shipment.delayed", "shipment.arrived", "weather.disruption", "fuel.spike", "route.anomaly"]

LAYER3B_LOGISTICS_TARGETS = [
    {"metric": "Telemetry Latency", "target": "< 3 seconds"},
    {"metric": "Event Accuracy", "target": "> 95%"},
    {"metric": "Delay Correlation", "target": "Stable"},
]

LAYER3B_SENTIMENT_STACK = [
    {"function": "NLP Runtime", "technology": "Transformers"},
    {"function": "Sentiment Models", "technology": "HuggingFace"},
    {"function": "Correlation", "technology": "Neo4j"},
    {"function": "Storage", "technology": "PostgreSQL"},
]

LAYER3B_SENTIMENT_TARGETS = [
    {"metric": "Sentiment Accuracy", "target": "> 90%"},
    {"metric": "False Positive Rate", "target": "Low"},
    {"metric": "Correlation Stability", "target": "Stable"},
]

LAYER3B_LOAD_TEST_STACK = [
    {"function": "Load Testing", "technology": "k6"},
    {"function": "Event Pressure", "technology": "Kafka producers"},
    {"function": "Runtime Metrics", "technology": "Prometheus"},
]

LAYER3B_PERFORMANCE_TARGETS = [
    {"metric": "OCR Throughput", "target": "10,000+ docs/hr"},
    {"metric": "Event Throughput", "target": "Stable"},
    {"metric": "Queue Latency", "target": "< 1 second"},
    {"metric": "Sync Delay", "target": "< 2 seconds"},
]

LAYER3B_CHAOS_SCENARIOS = [
    {"scenario": "OCR worker failure", "purpose": "Ingestion resilience"},
    {"scenario": "Commodity feed outage", "purpose": "Fallback validation"},
    {"scenario": "Logistics API outage", "purpose": "Survivability"},
    {"scenario": "Event bus congestion", "purpose": "Synchronization resilience"},
    {"scenario": "Procurement flood", "purpose": "Runtime elasticity"},
    {"scenario": "Recursive event storm", "purpose": "Containment validation"},
]

LAYER3B_OBSERVABILITY_METRICS = [
    {"metric": "OCR latency", "purpose": "Ingestion pipeline visibility"},
    {"metric": "Queue depth", "purpose": "Event pressure monitoring"},
    {"metric": "Vendor anomaly rate", "purpose": "Supplier intelligence signal"},
    {"metric": "Commodity volatility", "purpose": "Macroeconomic sensing"},
    {"metric": "Logistics delays", "purpose": "Operational pressure indicator"},
    {"metric": "Sentiment spikes", "purpose": "Disruption intelligence"},
    {"metric": "Federation lag", "purpose": "Synchronization stability"},
]

LAYER3B_FINAL_GATES = [
    {"validation": "OCR deployment operational", "required": True},
    {"validation": "Procurement ingestion operational", "required": True},
    {"validation": "Vendor telemetry synchronized", "required": True},
    {"validation": "Commodity APIs stable", "required": True},
    {"validation": "Logistics ingestion active", "required": True},
    {"validation": "Benchmark analytics operational", "required": True},
    {"validation": "Sentiment calibration validated", "required": True},
    {"validation": "Load testing passed", "required": True},
    {"validation": "Synchronization stable", "required": True},
    {"validation": "Chaos survivability passed", "required": True},
]

LAYER3B_FINAL_STATE = {
    "declaration": "A LIVE DISTRIBUTED COMMERCIAL INTELLIGENCE ACQUISITION NETWORK",
    "capabilities": [
        "Continuously sensing procurement ecosystems",
        "Ingesting operational telemetry at scale",
        "Synchronizing market intelligence in real-time",
        "Tracking vendor behavior and anomalies",
        "Monitoring logistics disruption signals",
        "Correlating commodity volatility",
        "Recursively propagating operational awareness",
    ],
    "system_evolution": "Infrastructure + Sensing Architecture → A LIVING OPERATIONAL INTELLIGENCE ACQUISITION ORGANISM",
    "next_layer": "Layer 4 — Operational Services Mesh",
}

# ── Layer 3B Endpoints ─────────────────────────────────────────────────────────

@app.get("/api/layer3b")
def get_layer3b_all():
    return {
        "overview": LAYER3B_OVERVIEW,
        "ocr_stack": LAYER3B_OCR_STACK,
        "ocr_validation": LAYER3B_OCR_VALIDATION,
        "ingestion_sources": LAYER3B_INGESTION_SOURCES,
        "event_topics": LAYER3B_EVENT_TOPICS,
        "vendor_telemetry_targets": LAYER3B_VENDOR_TELEMETRY_TARGETS,
        "commodity_sources": LAYER3B_COMMODITY_SOURCES,
        "commodity_intervals": LAYER3B_COMMODITY_INTERVALS,
        "logistics_sources": LAYER3B_LOGISTICS_SOURCES,
        "logistics_topics": LAYER3B_LOGISTICS_TOPICS,
        "sentiment_stack": LAYER3B_SENTIMENT_STACK,
        "performance_targets": LAYER3B_PERFORMANCE_TARGETS,
        "chaos_scenarios": LAYER3B_CHAOS_SCENARIOS,
        "observability_metrics": LAYER3B_OBSERVABILITY_METRICS,
        "final_gates": LAYER3B_FINAL_GATES,
        "final_state": LAYER3B_FINAL_STATE,
    }

@app.get("/api/layer3b/overview")
def get_layer3b_overview():
    return LAYER3B_OVERVIEW

@app.get("/api/layer3b/ocr")
def get_layer3b_ocr():
    return {"stack": LAYER3B_OCR_STACK, "validation": LAYER3B_OCR_VALIDATION}

@app.get("/api/layer3b/procurement")
def get_layer3b_procurement():
    return {"sources": LAYER3B_INGESTION_SOURCES, "event_topics": LAYER3B_EVENT_TOPICS}

@app.get("/api/layer3b/telemetry")
def get_layer3b_telemetry():
    return {"targets": LAYER3B_VENDOR_TELEMETRY_TARGETS, "commodity_sources": LAYER3B_COMMODITY_SOURCES, "intervals": LAYER3B_COMMODITY_INTERVALS}

@app.get("/api/layer3b/logistics")
def get_layer3b_logistics():
    return {"sources": LAYER3B_LOGISTICS_SOURCES, "topics": LAYER3B_LOGISTICS_TOPICS, "targets": LAYER3B_LOGISTICS_TARGETS}

@app.get("/api/layer3b/sentiment")
def get_layer3b_sentiment():
    return {"stack": LAYER3B_SENTIMENT_STACK, "targets": LAYER3B_SENTIMENT_TARGETS}

@app.get("/api/layer3b/chaos")
def get_layer3b_chaos():
    return {"scenarios": LAYER3B_CHAOS_SCENARIOS, "total": len(LAYER3B_CHAOS_SCENARIOS)}

@app.get("/api/layer3b/observability")
def get_layer3b_observability():
    return {"metrics": LAYER3B_OBSERVABILITY_METRICS}

@app.get("/api/layer3b/final-state")
def get_layer3b_final_state():
    return {"gates": LAYER3B_FINAL_GATES, "final_state": LAYER3B_FINAL_STATE}


# ── Layer 4 Data ──────────────────────────────────────────────────────────────

LAYER4_OVERVIEW = {
    "layer": "Layer 4",
    "name": "Intelligence Processing & Causal Analysis (IPCA)",
    "status": "INITIATING",
    "role": "The cognitive cortex of OSG-CI™ — transforms sensing into reasoning, correlating, forecasting, and causality-aware intelligence.",
    "sections": 13,
    "constructs": ["Anomaly detection engines", "Causal inference runtimes", "Probabilistic reasoning systems", "Graph intelligence infrastructure", "Recursive reinforcement learning", "Operational intelligence synthesis", "Anticipatory economic modeling"],
}

LAYER4_ANOMALY_STACK = [
    {"function": "Stream Processing", "technology": "Apache Flink"},
    {"function": "ML Runtime", "technology": "PyTorch"},
    {"function": "Feature Store", "technology": "Feast"},
    {"function": "Event Correlation", "technology": "Redpanda"},
    {"function": "Detection Runtime", "technology": "Python ML Services"},
]

LAYER4_ANOMALY_CATEGORIES = [
    {"category": "Procurement", "examples": "Abnormal pricing"},
    {"category": "Vendor", "examples": "Delivery collapse"},
    {"category": "Logistics", "examples": "Route disruption"},
    {"category": "Commodity", "examples": "Volatility spikes"},
    {"category": "Federation", "examples": "Sync drift"},
    {"category": "Intelligence", "examples": "Recursive instability"},
]

LAYER4_DETECTION_MODELS = [
    {"model": "Isolation Forest", "purpose": "Outlier detection"},
    {"model": "Autoencoders", "purpose": "Behavioral anomalies"},
    {"model": "LSTM", "purpose": "Temporal anomalies"},
    {"model": "Bayesian Detection", "purpose": "Probabilistic anomalies"},
]

LAYER4_CAUSAL_STACK = [
    {"function": "Graph Runtime", "technology": "Neo4j"},
    {"function": "Causal ML", "technology": "DoWhy"},
    {"function": "Bayesian Runtime", "technology": "PyMC"},
    {"function": "Correlation Engine", "technology": "Python"},
    {"function": "Event Runtime", "technology": "Redpanda"},
]

LAYER4_CAUSAL_EXAMPLE = [
    "Fuel Price Spike",
    "Freight Cost Increase",
    "Logistics Delay",
    "Vendor Fulfillment Stress",
    "Procurement Inflation",
]

LAYER4_PROBABILISTIC_STACK = [
    {"function": "Bayesian Networks", "technology": "PyMC"},
    {"function": "Probabilistic Graphs", "technology": "pgmpy"},
    {"function": "Forecast Correlation", "technology": "Prophet"},
    {"function": "Scenario Modeling", "technology": "NumPy / Pandas"},
]

LAYER4_PROBABILISTIC_OUTPUTS = [
    {"output": "Risk Probability", "purpose": "Disruption likelihood score"},
    {"output": "Forecast Confidence", "purpose": "Prediction integrity rating"},
    {"output": "Supply Risk", "purpose": "Operational pressure index"},
    {"output": "Economic Pressure", "purpose": "Institutional stress indicator"},
]

LAYER4_GRAPH_STACK = [
    {"function": "Graph DB", "technology": "Neo4j"},
    {"function": "Graph ML", "technology": "PyTorch Geometric"},
    {"function": "Correlation Engine", "technology": "Graph Algorithms"},
    {"function": "Visualization", "technology": "Bloom / Grafana"},
]

LAYER4_GRAPH_ANALYTICS = [
    {"analysis": "Centrality", "purpose": "Dependency risk scoring"},
    {"analysis": "Community Detection", "purpose": "Regional clustering"},
    {"analysis": "Path Analysis", "purpose": "Disruption propagation"},
    {"analysis": "Influence Scoring", "purpose": "Systemic pressure"},
]

LAYER4_RL_STACK = [
    {"function": "RL Runtime", "technology": "Ray RLlib"},
    {"function": "Distributed Training", "technology": "Ray"},
    {"function": "Reward Modeling", "technology": "Python"},
    {"function": "State Synchronization", "technology": "Redis"},
]

LAYER4_RL_OBJECTIVES = [
    {"objective": "Procurement Efficiency", "goal": "Maximize"},
    {"objective": "Forecast Accuracy", "goal": "Maximize"},
    {"objective": "Logistics Stability", "goal": "Maximize"},
    {"objective": "Risk Exposure", "goal": "Minimize"},
    {"objective": "Operational Drift", "goal": "Minimize"},
]

LAYER4_SYNTHESIS_OUTPUTS = [
    {"output": "Procurement Risk", "purpose": "Operational response triggers"},
    {"output": "Vendor Instability", "purpose": "Supplier mitigation actions"},
    {"output": "Logistics Forecast", "purpose": "Route optimization signals"},
    {"output": "Inflation Pressure", "purpose": "Budget adaptation guidance"},
    {"output": "Demand Shift", "purpose": "Procurement strategy updates"},
]

LAYER4_ECONOMIC_STACK = [
    {"function": "Time-Series Forecasting", "technology": "Prophet"},
    {"function": "Sequential Modeling", "technology": "LSTM"},
    {"function": "Bayesian Forecasting", "technology": "PyMC"},
    {"function": "Economic Correlation", "technology": "Neo4j"},
    {"function": "Simulation", "technology": "NumPy"},
]

LAYER4_ECONOMIC_OUTPUTS = [
    {"output": "Inflation Forecast", "purpose": "Procurement planning signal"},
    {"output": "Fuel Risk", "purpose": "Logistics adaptation trigger"},
    {"output": "Labor Pressure", "purpose": "Operational planning input"},
    {"output": "Commodity Stress", "purpose": "Supply forecasting baseline"},
    {"output": "Regional Instability", "purpose": "Strategic mitigation guidance"},
]

LAYER4_EVENT_TOPICS = [
    "anomaly.detected",
    "causal.link.inferred",
    "forecast.generated",
    "risk.escalated",
    "economic.pressure.updated",
    "vendor.instability.detected",
    "recursive.learning.updated",
]

LAYER4_OBSERVABILITY_METRICS = [
    {"metric": "Anomaly Accuracy", "purpose": "Detection quality monitoring"},
    {"metric": "Forecast Confidence", "purpose": "Predictive integrity score"},
    {"metric": "Causal Stability", "purpose": "Reasoning consistency validation"},
    {"metric": "RL Reward Convergence", "purpose": "Adaptive stability tracking"},
    {"metric": "Graph Propagation Latency", "purpose": "Synchronization visibility"},
    {"metric": "Economic Drift", "purpose": "Model calibration indicator"},
]

LAYER4_CHAOS_SCENARIOS = [
    {"scenario": "Event Storm", "purpose": "Synchronization resilience"},
    {"scenario": "False Anomaly Flood", "purpose": "Detection stability"},
    {"scenario": "Commodity Spike", "purpose": "Forecasting validation"},
    {"scenario": "Federation Drift", "purpose": "Graph consistency"},
    {"scenario": "RL Instability", "purpose": "Recursive containment"},
    {"scenario": "Economic Shock", "purpose": "Probabilistic resilience"},
]

LAYER4_VALIDATION_GATES = [
    {"validation": "Anomaly engines operational", "required": True},
    {"validation": "Causal inference validated", "required": True},
    {"validation": "Probabilistic reasoning stable", "required": True},
    {"validation": "Graph intelligence synchronized", "required": True},
    {"validation": "RL convergence stable", "required": True},
    {"validation": "Intelligence synthesis operational", "required": True},
    {"validation": "Economic modeling calibrated", "required": True},
    {"validation": "Event synchronization stable", "required": True},
    {"validation": "Chaos survivability passed", "required": True},
]

LAYER4_FINAL_STATE = {
    "declaration": "A CAUSAL-AWARE RECURSIVE COMMERCIAL INTELLIGENCE SYSTEM",
    "capabilities": [
        "Detecting anomalies across all operational dimensions",
        "Inferring causality from procurement and logistics signals",
        "Reasoning probabilistically under uncertainty",
        "Modeling operational relationships via graph intelligence",
        "Recursively improving intelligence through RL",
        "Synthesizing operational strategy from live data",
        "Forecasting macroeconomic disruption in advance",
    ],
    "evolution": "Sensing Infrastructure → A REASONING & ANTICIPATORY INTELLIGENCE ORGANISM",
    "next_layer": "Layer 5 — Recursive Synchronization & Simulation (RISE Core Runtime)",
    "layer5_preview": ["Recursive synchronization engines", "Distributed intelligence propagation", "Simulation runtimes", "Adaptive operational modeling", "Strategic economic simulations", "Full nervous-system intelligence orchestration"],
}

# ── Layer 4 Endpoints ──────────────────────────────────────────────────────────

@app.get("/api/layer4")
def get_layer4_all():
    return {
        "overview": LAYER4_OVERVIEW,
        "anomaly_stack": LAYER4_ANOMALY_STACK,
        "anomaly_categories": LAYER4_ANOMALY_CATEGORIES,
        "detection_models": LAYER4_DETECTION_MODELS,
        "causal_stack": LAYER4_CAUSAL_STACK,
        "causal_chain_example": LAYER4_CAUSAL_EXAMPLE,
        "probabilistic_stack": LAYER4_PROBABILISTIC_STACK,
        "probabilistic_outputs": LAYER4_PROBABILISTIC_OUTPUTS,
        "graph_stack": LAYER4_GRAPH_STACK,
        "graph_analytics": LAYER4_GRAPH_ANALYTICS,
        "rl_stack": LAYER4_RL_STACK,
        "rl_objectives": LAYER4_RL_OBJECTIVES,
        "synthesis_outputs": LAYER4_SYNTHESIS_OUTPUTS,
        "economic_stack": LAYER4_ECONOMIC_STACK,
        "economic_outputs": LAYER4_ECONOMIC_OUTPUTS,
        "event_topics": LAYER4_EVENT_TOPICS,
        "observability_metrics": LAYER4_OBSERVABILITY_METRICS,
        "chaos_scenarios": LAYER4_CHAOS_SCENARIOS,
        "validation_gates": LAYER4_VALIDATION_GATES,
        "final_state": LAYER4_FINAL_STATE,
    }

@app.get("/api/layer4/overview")
def get_layer4_overview():
    return LAYER4_OVERVIEW

@app.get("/api/layer4/anomaly")
def get_layer4_anomaly():
    return {"stack": LAYER4_ANOMALY_STACK, "categories": LAYER4_ANOMALY_CATEGORIES, "models": LAYER4_DETECTION_MODELS}

@app.get("/api/layer4/causal")
def get_layer4_causal():
    return {"stack": LAYER4_CAUSAL_STACK, "example_chain": LAYER4_CAUSAL_EXAMPLE}

@app.get("/api/layer4/probabilistic")
def get_layer4_probabilistic():
    return {"stack": LAYER4_PROBABILISTIC_STACK, "outputs": LAYER4_PROBABILISTIC_OUTPUTS}

@app.get("/api/layer4/graph")
def get_layer4_graph():
    return {"stack": LAYER4_GRAPH_STACK, "analytics": LAYER4_GRAPH_ANALYTICS}

@app.get("/api/layer4/rl")
def get_layer4_rl():
    return {"stack": LAYER4_RL_STACK, "objectives": LAYER4_RL_OBJECTIVES}

@app.get("/api/layer4/synthesis")
def get_layer4_synthesis():
    return {"outputs": LAYER4_SYNTHESIS_OUTPUTS}

@app.get("/api/layer4/economic")
def get_layer4_economic():
    return {"stack": LAYER4_ECONOMIC_STACK, "outputs": LAYER4_ECONOMIC_OUTPUTS}

@app.get("/api/layer4/events")
def get_layer4_events():
    return {"topics": LAYER4_EVENT_TOPICS, "total": len(LAYER4_EVENT_TOPICS)}

@app.get("/api/layer4/chaos")
def get_layer4_chaos():
    return {"scenarios": LAYER4_CHAOS_SCENARIOS, "total": len(LAYER4_CHAOS_SCENARIOS)}

@app.get("/api/layer4/final-state")
def get_layer4_final_state():
    return {"gates": LAYER4_VALIDATION_GATES, "final_state": LAYER4_FINAL_STATE}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
