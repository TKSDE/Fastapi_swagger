FROM postgres:latest

# Set environment variables
ENV POSTGRES_USER=va2pt
ENV POSTGRES_PASSWORD=va2ptpass
ENV POSTGRES_DB=va2ptdb

# Copy custom pg_hba.conf
COPY pg_hba.conf /var/lib/postgresql/data/pg_hba.conf

# Expose PostgreSQL port
EXPOSE 5432
