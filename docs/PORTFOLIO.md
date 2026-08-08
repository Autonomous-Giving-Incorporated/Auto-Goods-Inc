# Portfolio

The Portfolio Controller owns the `VentureCandidate` queue, compares candidates, assigns validation budgets, manages concentration, and promotes, holds, or kills by policy. It cannot control treasury, modify invariants, grade its own evidence, or bypass human gates.

## Initial limits
- Maximum active `ValidationExperiment` records: 5
- Maximum simultaneous builds: 2

Aggregate and per-venture spending are separately bounded. Decomposition cannot evade limits.

Prefer low proof cost, short time to revenue, high automation, low regulatory complexity, low support burden, reachable buyers, and behavioral evidence. Initially avoid medical decision software, individualized financial advice, physical inventory, heavily regulated marketplaces, custom enterprise consulting, and products requiring large support teams. Exceptions require human governance and qualified review.

Decisions compare evidence, expected value, proof cost, recovery time, concentration, capacity, security/regulatory exposure, and occupied-slot opportunity cost. Community need is not a commercial input. Promotion consumes a slot only after gates pass. `HOLD` requires a concrete unblock condition. `KILL` is appropriate when validation budget expires, buyer is falsified, acquisition or support breaks economics, legal/platform constraints invalidate the model, a substitute removes differentiation, or evidence confidence collapses. Record closure and reusable learning.
