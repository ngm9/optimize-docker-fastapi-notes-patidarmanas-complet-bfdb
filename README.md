### Task Overview
You are tasked with containerizing and optimizing a basic FastAPI-powered Notes API. The service lets users create, retrieve, and delete notes stored in-memory. While the current implementation is functional, the Docker setup is inefficient: every build fully reinstalls dependencies regardless of changes, build times are long, and the image is larger than needed. Your goal is to optimize the Dockerfile and deployment to align with modern best practices, focusing on build efficiency and image without touching the app's business logic.

# Application Access
- Host: <DROPLET_IP> (or localhost), Port: 8000
- Endpoints:
  - GET /notes
  - GET /notes/{note_id}
  - POST /notes
  - DELETE /notes/{note_id}
  - GET /healthz (readiness check)

### Objectives
- Optimize Dockerfile to take full advantage of build cache for dependencies.
- Use a lightweight and production-suitable base image.
- Implement a basic multi-stage build to separate build and production artifacts.
- Refine .dockerignore to exclude unneeded files from the image/context.
- Verify the FastAPI app runs reliably in Docker, with all endpoints functional.

### How to Verify
- Build the Docker image twice and confirm that the second build uses cached layers and finishes quickly.
- Inspect the final image size after optimization and confirm a reduction compared to initial state.
- Run the FastAPI container, access all endpoints, and ensure JSON responses are correct.
- Inspect Docker logs to ensure application starts without error.
- Check that no development/test files are present in the runtime container.

### Helpful Tips
- Consider reordering Dockerfile instructions to enable dependency layer reuse.
- Review which files need to be inside the final container for correct operation.
- Think about how to keep artifacts and dependencies separate from source code.
- Explore how to choose a base image that balances compatibility with performance.
- Check what is included/excluded via .dockerignore and how that impacts the build context.
