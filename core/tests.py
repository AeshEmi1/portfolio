from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse


class PortfolioTests(TestCase):
    """Contains test cases for my portfolio."""

    def test_pages_load_successfully(self) -> None:
        """Verify all static pages are reachable and return a 200 OK status."""
        pages = ["index", "projects", "contact"]
        for page in pages:
            response: HttpResponse = self.client.get(reverse(page))  # type: ignore
            self.assertEqual(
                response.status_code, 200, f"Page '{page}' failed to load."
            )

    def test_critical_content_exists(self) -> None:
        """Confirm your name or key headings are present so the page isn't blank."""
        response: HttpResponse = self.client.get(reverse("index"))  # type: ignore
        # Replace 'Your Name' with the actual text in your <h1> or title
        self.assertContains(response, "Emiliano Garcia", html=True)
        self.assertContains(response, "Cybersecurity Engineer")

    def test_navigation_links_present(self) -> None:
        """Verify the navigation bar has links to other sections."""
        response: HttpResponse = self.client.get(reverse("index"))  # type: ignore
        # This checks if the HTML contains the expected href links
        self.assertContains(response, f'href="{reverse("projects")}"')
        self.assertContains(response, f'href="{reverse("contact")}"')

    def test_404_handler(self) -> None:
        """Verify that a garbage URL returns a 404 instead of a server error."""
        response: HttpResponse = self.client.get("/this-page-does-not-exist/")  # type: ignore
        self.assertEqual(response.status_code, 404)
