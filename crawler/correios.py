from selenium import webdriver
import pandas as pd


class HtmlObject:
    """Class for the HTML element for search"""

    def __init__(self, url, driver=None):
        self.driver = driver
        self.url = url
        self.name_select_ufs = "UF"
        self.tag_name_ufs = "option"
        self.__ufs = None
        self.location_table_xpath = '(//table[@class="tmptabela"])[last()]'
        self.btn_search = 'input[value="Buscar"]'

    def search_url(self):
        """Navigates to the link in self.url"""
        self.driver.get(self.url)

    @property
    def ufs(self):
        """Returns an array with all the ufs specified in the page"""
        if not self.__ufs:
            select_ufs = self.driver.find_element_by_name(self.name_select_ufs)
            options = [
                uf.text
                for uf in select_ufs.find_elements_by_tag_name(self.tag_name_ufs)
            ]

            self.__ufs = list(filter(lambda x: bool(x) is not False, options))
        return self.__ufs

    def _search_uf(self, uf):
        """Search for a uf"""
        select_ufs = self.driver.find_element_by_name(self.name_select_ufs)
        select_ufs.find_element_by_css_selector(
            f"{self.tag_name_ufs}[value={uf}]"
        ).click()
        btn_search = self.driver.find_element_by_css_selector(self.btn_search)
        btn_search.click()

    def uf_locations(self):
        """
        Creates a data frame with the fields 'Localidade' and 'Faixa de CEP'"""
        location_table = self.driver.find_element_by_xpath(self.location_table_xpath)
        df_table = pd.read_html(
            "<table>" + location_table.get_attribute("innerHTML") + "</table>"
        )
        return df_table[0][["Localidade", "Faixa de CEP"]]

    def export_jsonl(self, data, filename):
        """Exports to the format jsonlines"""
        jsonl = data.to_json(orient="records", lines=True)
        with open(filename, mode="w", encoding="utf-8") as file:
            for line in jsonl:
                file.write(line)

    def search_all_ufs(self):
        """Collect the data for all ufs"""
        for uf in self.ufs:
            self._search_uf(uf)
            df_locations = self.uf_locations()
            self.export_jsonl(df_locations, f"data/{uf}.jsonl")
            self.driver.back()
