# Generation Method — Local Process Record

This file documents how the Cambium sourcebook was assembled. It is process provenance and is deliberately excluded from the NotebookLM product notebook.

- The Meristem listener executed the configured brand pipeline one bounded skill at a time.
- Each skill produced a validated JSON receipt under `.brandmint/outputs/`.
- Text receipts informed an authored product packet; raw generated Markdown prompts and pipeline outputs were not uploaded as NotebookLM sources.
- Visual concepts were rendered through the logged-in Codex image-generation session, not an API-credit integration.
- Every accepted visual has a local file, dimensions, a SHA-256 digest, and an origin receipt in its corresponding pipeline output.
- Generated product scenes and interfaces are labeled conceptual rather than presented as shipping-product proof.
- NotebookLM receives only the five documents in `notebooklm/product-sources/`.

The purpose of the separation is epistemic clarity. The product notebook should answer questions about Cambium. It should not mistake how the packet was generated for what the product is.

