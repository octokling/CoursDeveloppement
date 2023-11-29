<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method = "html" encoding="ASCII" />
	
	<xsl:template match="films">	
		<html>
			<title>Coucou</title>
			<body>
				<xsl:for-each select="film">
					Titre du film : <xsl:value-of select = "titre"/><br/>
					Genre : <xsl:value-of select = "genre"/><br/>
					Acteurs : <ul>
					<xsl:for-each select="./acteurs/personne">
						<li><xsl:value-of select="."/></li>
					</xsl:for-each>
					</ul>
					<xsl:variable name="val" select="./realisateur/@codartiste"></xsl:variable> 
					Réalisateur : <xsl:value-of select = "/basefilms/artistes/artiste[@codartiste=$val]/nom"/><br/> 
					<br/> 
				</xsl:for-each>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>