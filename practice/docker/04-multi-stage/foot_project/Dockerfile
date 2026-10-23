FROM gcc:latest AS builder
WORKDIR /app
COPY foot.c .
RUN gcc foot.c -static -o foot
RUN ls -l /app
FROM scratch
COPY --from=builder /app/foot /app/foot
ENTRYPOINT ["/app/foot"]
