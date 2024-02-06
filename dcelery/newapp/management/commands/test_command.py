from django.core.management.base import BaseCommand, CommandError
from typing import Any, Optional

class Command(BaseCommand):
    help = "test command description"
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("This is my simple task")
        